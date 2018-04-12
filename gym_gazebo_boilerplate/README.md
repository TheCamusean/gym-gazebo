# Gym-Gazebo Boilerplate (also useful for real robots)

This boilerplate has been designed with the idea of making easier the development of new gym enviroments without deep knowledge of python and particularlly applicable in Gazebo.

## Steps

The following ionstructions are the modifications that you should do in gym_gazebo_boilerplate in order to make it work in your own enviroment:

1. Copy the package gym_gazebo_boilerplate to your own enviroment and set the name you wish in both the main folder and the folder gym_gazebo_boilerplate/gym_gazebo_boilerplate.

2. Set in setup.py the new name of your package

3. Install the package:

```
sudo pip install -e .
```

4. In gym_gazebo_boilerplate/gym_gazebo_boilerplate/envs/box/gazebo_box.py is defined the main gym functions for your particular enviroment. Here you should define step() , reset() ...

5. In gym_gazebo_boilerplate/gym_gazebo_boilerplate/envs/box/__init__.py , import your new class

6. In order to make gym recognize your enviroment you have to register the new class as an enviroment. do that in gym_gazebo_boilerplate/gym_gazebo_boilerplate/__init__.py

7. Once you want to use your enviroment, in gym_gazebo_boilerplate/examples/box/box_gym.py, you should import your new package, installed with the name set in step 2.



