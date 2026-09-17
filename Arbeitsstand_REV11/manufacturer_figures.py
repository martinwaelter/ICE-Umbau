"""Lossless viewports over unchanged 600 dpi renders of original Märklin pages.

No source image is cropped, rotated, repainted, or rewritten.  ReportLab clips the
unchanged full-page bitmap to a verified viewport.  Coordinates are normalized
from the upper left: (left, top, right, bottom).
"""
from pathlib import Path
from reportlab.platypus import Flowable
from PIL import Image

ROOT = Path(__file__).resolve().parent
SOURCE_ROOT = ROOT / 'zeichnungsquellen'

FIGURES = {
    'motor_60941': {
        'path': SOURCE_ROOT / 'maerklin_60941_seite2_600dpi.png',
        'crop': (.100, .030, .875, .625),
        'source_pdf': ROOT.parent / 'Pruefnachweise/REV9_Berichtsabgleich/Maerklin_60941_Original.pdf',
        'source_page': 2,
        'caption': 'Märklin 60941/60943, Originalzeichnung S. 2: Ausbau links, Einbau rechts. Bildnummern 1–6 aus der Herstellerzeichnung.',
    },
    'carrier_60977': {
        'path': SOURCE_ROOT / 'maerklin_60977_600dpi-005.png',
        'crop': (.045, .225, .478, .695),
        'source_pdf': ROOT.parent / 'Pruefnachweise/REV9_Berichtsabgleich/Maerklin_60977_Original.pdf',
        'source_page': 5,
        'caption': 'Märklin-Träger, Originalzeichnung S. 5. Padnamen und Märklin-Kabelfarben; im Gegenkopf wird der ESU 59649 eingesetzt.',
    },
    'insertion_21mtc': {
        'path': SOURCE_ROOT / 'maerklin_60977_600dpi-006.png',
        'crop': (.070, .205, .375, .910),
        'source_pdf': ROOT.parent / 'Pruefnachweise/REV9_Berichtsabgleich/Maerklin_60977_Original.pdf',
        'source_page': 6,
        'caption': 'Märklin, Originalzeichnung S. 6: Einsteckfolge mit vergrößertem Warn-Seitenprofil. Kein Foto des eingebauten ESU-Decoders.',
    },
}


class ManufacturerFigure(Flowable):
    """Place one original drawing at a bounded width and optionally height.

    Example: story.append(ManufacturerFigure('motor_60941', width=510,
                                            max_height=280))
    The resulting width and height are the actual viewport dimensions.
    Each instance keeps its natural aspect ratio and aligns left by default.
    """
    def __init__(self, kind, width=510, max_height=None, hAlign='LEFT'):
        super().__init__()
        if kind not in FIGURES:
            raise ValueError(f'Unknown drawing: {kind}')
        self.kind = kind
        self.spec = FIGURES[kind]
        self.path = str(self.spec['path'])
        self.crop = self.spec['crop']
        with Image.open(self.path) as im:
            self.image_width, self.image_height = im.size
        left, top, right, bottom = self.crop
        assert 0 <= left < right <= 1 and 0 <= top < bottom <= 1
        natural_width = (right - left) * self.image_width
        natural_height = (bottom - top) * self.image_height
        self.scale_factor = width / natural_width
        if max_height is not None:
            self.scale_factor = min(self.scale_factor, max_height / natural_height)
        self.width = natural_width * self.scale_factor
        self.height = natural_height * self.scale_factor
        self.hAlign = hAlign

    @property
    def effective_dpi(self):
        return 72 / self.scale_factor

    def draw(self):
        c = self.canv
        left, top, right, bottom = self.crop
        scale = self.scale_factor
        iw, ih = self.image_width, self.image_height
        c.saveState()
        window = c.beginPath()
        window.rect(0, 0, self.width, self.height)
        c.clipPath(window, stroke=0, fill=0)
        c.drawImage(self.path, -left * iw * scale, -(1 - bottom) * ih * scale,
                    width=iw * scale, height=ih * scale)
        c.restoreState()


def manufacturer_figure(kind, width=510, max_height=None, hAlign='LEFT'):
    return ManufacturerFigure(kind, width, max_height, hAlign)
