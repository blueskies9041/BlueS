/*
	PROJECT INFORMATION

		Name: SamOGL
		Brief: Beginnings of Samuel Legus's AIE Assessment 4 Project

		* Significant Changes:
			MOTHER FUCKING TEXT

		* To Do
			Make something like a game.
			Particles!

				
	LAST RECORDED EDITS ON: March 04, 2014
*/

#include "glew.h"
#include "glfw3.h"
#include "Player.h"
#include <iostream>
#include "Text.h"
#include "Timer.h"
#include "Window.h"

using namespace std;

void main()
{
	/* Test Objects */

	Timer::Instance();
	Window::Instance().Initialize(1024, 768, "Hello!");

	//Text T("resources/graphics/Holstein.png");
	//Text Z("resources/graphics/Holstein2.png");	

	Sprite SpriteA("resources/graphics/ZeroSpriteSheet.png", 200, 200, 75, 75, Window::Instance().Context());
	Player Player1;
	
	//SpriteA.m_v3Position.x += 150.0f;

	//ResetDeltaTime();
	/* Main Loop */
	while (!glfwWindowShouldClose(Window::Instance().Context()))
	{	
		Timer::Instance().Update();
		Window::Instance().Update();

        /* Poll for and process events */
		if(GLFW_PRESS == glfwGetKey(Window::Instance().Context(), GLFW_KEY_ESCAPE))
			glfwSetWindowShouldClose(Window::Instance().Context(), true);

		
		Justin::glfw_update_fps_counter(Window::Instance().Context());

	
    }

	
	glfwTerminate();
}

