import tempfile
import unittest
from pathlib import Path

from svm11.qc import fill, selfqc


class DraftQCTest(unittest.TestCase):
    def test_selfqc_and_fill_before_lock_from_repo_export(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            (base / "exports").mkdir()
            (base / "assets").mkdir()
            (base / "assets/frames.csv").write_text("frame,file,cx,cy,r\n0,f.jpg,50,50,100\n")
            (base / "exports/r1.xml").write_text('''<annotations><version>1.1</version>
            <meta><task><name>raw_fisheye</name></task></meta>
            <image id="0" name="f.jpg" width="100" height="100">
            <box label="Car" xtl="10" ytl="10" xbr="50" ybr="60" group_id="4"/>
            <polygon label="Car" group_id="4" points="10,10;50,10;50,60;10,60"/>
            </image></annotations>''')
            qc = selfqc(base, "r1_craft")
            self.assertTrue(qc.is_file())
            qc.write_text(qc.read_text().replace("- [ ] Class sáu nhãn", "- [x] Class sáu nhãn"))
            self.assertIn("- [x] Class sáu nhãn", selfqc(base, "r1_craft").read_text())
            filled = fill(base, "r1_craft")
            self.assertIn("Fill ratio (K12)", filled.read_text())


class SelfQCFrameTest(unittest.TestCase):
    def test_frame_missing_from_frames_csv_fails_even_without_boxes(self):
        from svm11 import LabError
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            (base / "exports").mkdir()
            (base / "assets").mkdir()
            (base / "assets/frames.csv").write_text("frame,file,cx,cy,r\n0,f.jpg,50,50,100\n")
            (base / "exports/r1.xml").write_text('<annotations><version>1.1</version>'
                                                 '<image id="0" name="g.jpg" width="100" height="100"/></annotations>')
            with self.assertRaises(LabError):
                selfqc(base, "r1_craft")
