# Self-Driving Cars: Projects & Assignments

This repository contains a collection of projects and assignments focused on **Autonomous Driving Systems**, covering fundamental concepts such as perception, mapping, localization, planning, and control. Each module is implemented in Python or Jupyter Notebooks, with the goal of building intuition and practical understanding of how self-driving cars operate.

---

## Projects

### Perception
- **Applying Stereo Depth to a Driving Scenario**  
  Estimate depth from stereo images to perceive the 3D structure of the environment.
    - Stereo Left and Right Image:
      ![Environment](media/stereo_1.png)
    - Stereo Disparity Map:
      ![Environment](media/stereo_disparity_map.png)
    - Stereo Depth Map:
      ![Environment](media/stereo_depth_map.png)
    - Object To Detect:
      ![Environment](media/stereo_object_to_detect.png)
    - Location of the object in the image:
      ![Environment](media/stereo_object_location.png)
    - Identification of object in Image:
      ![Environment](media/stereo_object_identification.png)
  
- **Lidar Parameter Estimation and Plane Fitting**  
  Extract ground planes and environmental features from LiDAR point clouds.

---

### Mapping
- **Occupancy Grid Mapping Using Inverse Measurement Model**  
  Implement probabilistic occupancy grid mapping for environment representation using Lidar Data.
  - Actual Environment where vehicle navigates:
  ![Environment](media/occupancy_map.gif)
  - What vehicles captures at every step about Environment:
  ![Environment Build](media/occupancy_map2.gif)
  - How occupancy grid is constructed as time progress:
  ![Occupancy Map](media/occupancy_map3.gif)

---

### Localization
- **Extended Kalman Filter**  
  Apply EKF for state estimation of a vehicle navigating through uncertain environments.

---

### Vehicle Dynamics & Control
- **Longitudinal Vehicle Model**  
  Model the longitudinal dynamics (acceleration/braking) of a car.
    - We will now drive the vehicle over a slope as shown in the diagram below:
    ![ramp](Longitudinal_Vehicle_Model/artifacts/ramp.png)
    - To climb the slope, a trapezoidal throttle input is provided for the next 20 seconds as shown in the figure below:
    ![throttle](Longitudinal_Vehicle_Model/artifacts/throttle.png)
    - After applying the throttle to the vehicle Longitudinal model we get the following about position of vehicle at every time step:
    ![Position vs Time](media/lonitudinal_output.png)

- **Kinematics Bicycle Model**  
  Explore the kinematic bicycle model for lateral vehicle motion.
    - Circle Path With Slip Angle:
    ![circle_path](media/kinematic_circle_path_with_slip_angle.png)
    - Circle Path Without Slip Angle:
    ![circle_path](media/kinematic_circle_path_without_slip_angle.png)
    - Square Path With Slip Angle:
    ![square_path](media/kinematic_square_path_with_slip_angle.png)
    - Square Path Without Slip Angle:
    ![square_path](media/kinematic_square_path_without_slip_angle.png)
    - Spiral Path With Slip Angle:
    ![square_path](media/kinematic_spiral_path.png)
    - Figure 8 Path With Slip Angle:
    ![square_path](media/kinematic_figure_8.png)

---

### Planning
- **Mission Planning**  
  Design algorithms like Dijkstra’s and $A^*$ for high-level route and trajectory shortest path planning in Berkeley, California.
  - Networkx Libraries Shortest Path for Reference:
  ![Reference](media/mission_planning_reference.png)
  - Dijkstra's Shortest Path:
  ![Dijkstras](media/mission_planning_with_dijkstras.png)
  - $A^*$ Shortest Path:
  ![Astar](media/mission_planning_with_A_star.png)

---

### Estimation & Learning
- **Ordinary Least Squares**  
  Apply OLS regression for parameter estimation tasks in driving scenarios.  

- **Recursive Least Squares**  
  Implement RLS for online, adaptive parameter estimation.