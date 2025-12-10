# harmonic_drives.py
from dataclasses import dataclass

@dataclass
class HarmonicDrive:
    name: str           # модель актуатора
    gear_ratio: float   # передаточное число N
    armature_inertia: float  # инерция на оси сустава (GD^2/4), kg·m^2
    mass: float         # масса актуатора, kg
    radius: float       # радиус цилиндра корпуса, m
    length: float       # длина цилиндра, m
    max_torque: float   # Maximum Torque, N·m


SHA20A_101 = HarmonicDrive(
    name="SHA20A-101",
    gear_ratio=101.0,
    armature_inertia=0.91,
    mass=2.0,
    radius=0.047,
    length=0.103,
    max_torque=107.0,
)

SHA25A_101 = HarmonicDrive(
    name="SHA25A-101",
    gear_ratio=101.0,
    armature_inertia=2.2,
    mass=5.0,
    radius=0.057,
    length=0.109,
    max_torque=204.0,
)

SHA32A_101 = HarmonicDrive(
    name="SHA32A-101",
    gear_ratio=101.0,
    armature_inertia=8.0,
    mass=2.95,
    radius=0.073,
    length=0.125,
    max_torque=433.0,
)


# Набор актуаторов на суставы (базовый вариант)

joint_variants = {
    # плечевые суставы – самые нагруженные → всегда SHA32A
    "shoulder_pan_joint":  [SHA32A_101],
    "shoulder_lift_joint": [SHA32A_101],

    # локоть: два варианта – полегче и помощнее
    "elbow_joint":         [SHA25A_101, SHA32A_101],

    # запястья: лёгкий SHA20A или более мощный SHA25A
    "wrist_1_joint":       [SHA20A_101, SHA25A_101],
    "wrist_2_joint":       [SHA20A_101, SHA25A_101],
    "wrist_3_joint":       [SHA20A_101, SHA25A_101],
}