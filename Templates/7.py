from manim import *
import numpy as np

class ChaosPendulum(Scene):
    def construct(self):
        # 设置混沌摆的参数
        L = 1.0  # 摆长
        g = 9.81  # 重力加速度
        m = 1.0  # 摆的质量（在此示例中未使用，但可用于更复杂的模拟）
        theta0 = PI / 6  # 初始角度
        omega0 = 0.5  # 初始角速度

        # 初始化位置和速度
        theta = theta0
        omega = omega0
        dt = 0.01  # 时间步长
        frames = 1000  # 总帧数

        # 用于存储摆的位置，以便动画化
        pendulum_points = []

        # 模拟混沌摆的运动
        for _ in range(frames):
            d2theta_dt2 = -(g / L) * np.sin(theta)
            omega += d2theta_dt2 * dt
            theta += omega * dt
            pendulum_bob = np.array([L * np.sin(theta), -L * np.cos(theta), 0])
            pendulum_points.append(pendulum_bob)

        # 创建空的 VMobject 来存储摆的点
        pendulum_mobject = VMobject()
        for point in pendulum_points:
            pendulum_mobject.add(Dot(point))

        # 动画展示
        self.play(Create(pendulum_mobject), run_time=frames * dt)
        self.wait()

