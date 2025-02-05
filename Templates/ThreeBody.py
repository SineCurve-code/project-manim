from manim import *

class ThreeBodyProblem(Scene):
    def construct(self):
        # 定义三个天体的初始位置和速度
        positions = [
            np.array([-2, 1, 0]),
            np.array([2, 1, 0]),
            np.array([0, -1, 0])
        ]
        velocities = [
            np.array([1, 0, 0]),
            np.array([-1, 0, 0]),
            np.array([0, 1, 0])
        ]

        # 创建三个点表示天体
        bodies = [Dot(point=pos).set_color(color) for pos, color in zip(positions, [RED, GREEN, BLUE])]

        # 添加天体到场景中
        for body in bodies:
            self.add(body)

        # 定义引力常数
        G = 1

        # 定义时间步长
        dt = 0.01

        # 定义动画
        def update_bodies(bodies, positions, velocities, dt):
            new_positions = []
            new_velocities = []
            for i in range(len(bodies)):
                total_force = np.zeros(3)
                for j in range(len(bodies)):
                    if i != j:
                        r = positions[j] - positions[i]
                        distance = np.linalg.norm(r)
                        force = G * r / distance**3
                        total_force += force
                new_velocity = velocities[i] + total_force * dt
                new_position = positions[i] + new_velocity * dt
                new_positions.append(new_position)
                new_velocities.append(new_velocity)
            return new_positions, new_velocities

        # 更新天体的位置
        def update(bodies, positions, velocities, dt):
            new_positions, new_velocities = update_bodies(bodies, positions, velocities, dt)
            for i in range(len(bodies)):
                bodies[i].move_to(new_positions[i])
            return new_positions, new_velocities

        # 运行动画
        for _ in range(500):  # 500帧
            positions, velocities = update(bodies, positions, velocities, dt)
            self.wait(dt)

# 运行场景
if __name__ == "__main__":
    scene = ThreeBodyProblem()
    scene.render()