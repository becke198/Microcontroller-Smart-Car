# Microcontroller-Smart-Car
Autonomous Vehicle Project

# Overview

This project focuses on the design and implementation of a low-cost Autonomous Vehicle (AV) capable of navigating a grid system with known obstacles. Using a wavefront pathfinding algorithm, our AV determines the shortest path from a starting point to an endpoint while avoiding collisions.

The project demonstrates the integration of hardware (BBC Micro:Bit, motors, sensors, and a custom 3D-printed frame) with software (Python-based algorithm) to achieve real-world navigation tasks.



# Features

Wavefront Algorithm for efficient shortest-path navigation.

Custom 3D-Printed Frame to house electronics and improve stability.

BBC Micro:Bit + robot:bit Expansion Board for motor and sensor control.

Obstacle Detection through map-based planning.

# Design Considerations

Drive System: Implemented using two DC motors with wheel power calibration.

Calibration Adjustments: Motor ratio fine-tuning for drift correction.

Sensors: Explored ultrasonic and compass integration (ultimately limited by inaccuracy).

Pathfinding: Robust wavefront algorithm ensuring efficient path discovery.

# Performance Summary

The algorithm successfully found the shortest path with 100% accuracy in simulation.

Hardware limitations (motor inconsistencies, battery drain, traction issues) caused drift, resulting in the AV finishing ~3 grid cells off target.

Attempts to improve accuracy via compass calibration, ultrasonic sensors, and wheel-speed ratios were partially effective but not fully reliable.

# Results & Lessons Learned

Algorithm: Performed correctly, providing valid navigation instructions.

Hardware: Limited precision of DC motors was the largest performance bottleneck.

Compass Feature: Too inaccurate due to magnetic interference and delays.

Testing Insight: Calibration must adapt dynamically to battery levels and motor wear.

## Recommendations for Future Work

Replace DC motors with encoders for precise movement tracking.

Use gyroscopes or accelerometers instead of (or alongside) a compass for orientation.

Implement dynamic calibration to adjust for drift in real-time.

Test across multiple surfaces and conditions for robustness.
