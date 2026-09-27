"""Paths, configuration, and small file helpers."""
import csv
import hashlib
import json
import os
from pathlib import Path

from . import LabError

ROUNDS = {"calib": "p1_calib", "r1_craft": "r1_craft", "rework": "rework"}


def root(value=None):
    return Path(value or os.environ.get("LAB11_ROOT") or Path(__file__).resolve().parent.parent).resolve()


def read_json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise LabError("Không đọc được %s: %s" % (path, exc)) from exc


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def slices(base):
    data = read_json(base / "assets" / "slices.json")
    result = {item["slice"]: item["frames"] for item in data.get("slices", [])}
    if "C0" in data:
        result["C0"] = [data["C0"]["frame"]]
    return result


def chosen_slice(base, round_name="r1_craft"):
    path = base / "submission" / "00_setup" / "mode.json"
    data = read_json(path)
    if round_name == "calib":
        return "C0"
    value = data.get("slice") or data.get("own_slice")
    if not value:
        raise LabError("Chưa chọn slice — chạy make mode hoặc make cvat SLICE=...")
    return value


def round_dir(base, round_name):
    if round_name not in ROUNDS:
        raise LabError("ROUND không hợp lệ: " + round_name)
    return base / "submission" / ROUNDS[round_name]


def digest(data):
    return hashlib.sha256(data).hexdigest()


def code(digest_value):
    value = digest_value[:8].upper()
    return value[:4] + "-" + value[4:]


def circles(base):
    path = base / "assets" / "frames.csv"
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return {row["file"]: (float(row["cx"]), float(row["cy"]), float(row["r"]))
                for row in csv.DictReader(stream)}
