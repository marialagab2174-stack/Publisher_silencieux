import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class StatusPub(Node):
    def __init__(self):
        super().__init__('status_publisher')
        # CORRECTION BUG 1 : Ajout du '/' pour un namespace global propre
        self.pub = self.create_publisher(String, '/robot/status', 10)
        self.timer = self.create_timer(1.0, self.cb)
        self.get_logger().info('Publisher corrigé et démarré sur /robot/status')

    def cb(self):
        # CORRECTION BUG 2 : Instanciation de la classe String() avec parenthèses
        msg = String()
        msg.data = 'OK'
        # CORRECTION BUG 3 : Passage de l'objet msg en argument de la fonction publish
        self.pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = StatusPub()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
