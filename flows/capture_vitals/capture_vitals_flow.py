from screens.capture_vitals.capture_vitals_screen import CaptureVitalsScreen
from keyword_core.page_provider import get_page
from values.capture_vitals import CaptureVitals


class CaptureVitalsFlow:
    def __init__(self):
        self.page = get_page()
        self.capture_vitals_screen = CaptureVitalsScreen(self.page)

    def capture_vitals(self, capture_vitals: CaptureVitals):
        pass  # TODO: Navigate to Patient list → patient detail → vitals page and capture vitals
