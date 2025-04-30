from dataclasses import asdict
import json
from pathlib import Path
from typed_urdf import Robot

robot = Robot.from_urdf(Path("asset/gp25.urdf"))
print(json.dumps(asdict(robot), indent=2))

robot_custom = robot.customize({"visual_basedir": "asset"})
print(json.dumps(asdict(robot_custom.links[0].visuals[0]), indent=2))

robot_custom = robot.customize({"visual_basedir": "http://example.com:8080"})
print(json.dumps(asdict(robot_custom.links[0].visuals[0]), indent=2))