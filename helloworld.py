#include<unistd.h>
#include"rclcpp/rclcpp.hpp"   //ros2 C++接口


class HelloWorldNode:public rclcpp::Node
{
public:
    HelloWorldNode():Node("node_helloworld") 
    {
        while(rclcpp::ok())
        {
            RCLCPP_INFO(this->get_logger(),"hello world! ros2");
            sleep(1);
        }
    }
};

int main(int argc,char*argv[])
{

    rclcpp::init(argc,argv);

    rclcpp::spin(std::make_shared<HelloWorldNode>());

    rclcpp::shutdown();
    return 0;
}





