from manim import *
from math import sin, cos

class ChaoticPendulum(Scene):
    def construct(self):
        # 物理参数设置
        g = 9.8  # 重力加速度
        lengths = [2.0, 1.5, 1.0]  # 各段摆长
        masses = [1.0, 0.8, 0.5]   # 各质点质量
        angles = [PI/2 + 0.1, PI/2 + 0.2, PI/2 + 0.3]  # 初始角度
        ang_velocities = [0.0, 0.0, 0.0]  # 初始角速度
        dt = 0.02  # 时间步长

        # 创建摆的组件
        points = []
        lines = []
        
        # 初始化各段摆的位置
        for i in range(3):
            x = sum(lengths[j] * sin(angles[j]) for j in range(i+1))
            y = -sum(lengths[j] * cos(angles[j]) for j in range(i+1))
            point = Dot(radius=0.1, color=RED).move_to([x, y, 0])
            points.append(point)
            
            if i == 0:
                line = Line(ORIGIN, point.get_center(), stroke_width=2)
            else:
                line = Line(points[i-1].get_center(), point.get_center(), stroke_width=2)
            lines.append(line)

        # 创建轨迹对象
        trail = TracedPath(points[-1].get_center, stroke_width=2, stroke_color=YELLOW)  # 跟踪最后一个质点
        self.add(trail, *points, *lines)

        # 定义物理更新函数
        def update_system(dt):
            nonlocal angles, ang_velocities
            
            # 计算各段的角加速度
            ang_accelerations = []
            for i in range(3):
                # 简化的物理模型（实际应使用拉格朗日方程）
                acc = -g / lengths[i] * sin(angles[i])
                if i < 2:  # 添加相邻摆的影响
                    acc += 0.5 * (ang_velocities[i+1]**2 * sin(angles[i+1]-angles[i]))
                ang_accelerations.append(acc)
                
            # 更新角度和角速度
            for i in range(3):
                ang_velocities[i] += ang_accelerations[i] * dt
                angles[i] += ang_velocities[i] * dt
                
            # 更新图形位置
            for i in range(3):
                x = sum(lengths[j] * sin(angles[j]) for j in range(i+1))
                y = -sum(lengths[j] * cos(angles[j]) for j in range(i+1))
                points[i].move_to([x, y, 0])
                
                if i == 0:
                    lines[i].put_start_and_end_on(ORIGIN, points[i].get_center())
                else:
                    lines[i].put_start_and_end_on(
                        points[i-1].get_center(), 
                        points[i].get_center()
                    )

        # 添加持续更新
        self.add_updater(update_system)
        self.wait(15)  # 运行动画时长
        self.remove_updater(update_system)