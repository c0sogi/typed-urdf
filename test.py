from dataclasses import asdict
from pathlib import Path
from typed_urdf import Robot

robot = Robot.from_urdf(Path("asset/gp25.urdf"))
print(asdict(robot))