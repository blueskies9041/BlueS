#ifndef _STATE_H_
#define _STATE_H_

#include <iostream>

using std::cout;
using std::endl;

struct State
{
	void (*Callback)(void); // Function Pointer, can be set to any other void function with no parameters.
};

inline void UpdateState(const State * a_opState)
{
	a_opState->Callback();
}

inline void UpdateMenu()
{
	static int iCallCount = 0;
	cout << "Menu State! Calls: " << iCallCount << endl;
	iCallCount++;
}

inline void UpdateGame()
{
	static int iCallCount = 0;
	cout << "Game State! Calls: " << iCallCount << endl; 
	iCallCount++;
}

inline void UpdateLoading()
{	
	static int iCallCount = 0;
	cout << "Loading State! Calls: " << iCallCount << endl; 
	iCallCount++;
}

#endif