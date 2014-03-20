#include <iostream>
#include "State.h"
#include "Stack.h"

using std::cout;
using std::endl;
using std::cin;

int main()
{
	State * GameState = new State;
		GameState->Callback = UpdateGame;
	State * MenuState  = new State;
		MenuState->Callback = UpdateMenu;
	State * LoadState  = new State;
		LoadState->Callback = UpdateLoading;

	Stack<State> StateStack(5);

	char cInput = 0;
	while(1)
	{
		cout << "Input Options : (1) Menu (2) Game (3) Load " << endl;
		cin >> cInput;
		switch(cInput)
		{
			case '1':
				StateStack.Pop();
				StateStack.Push(*MenuState);
				break;
			case '2':
				StateStack.Pop();
				StateStack.Push(*GameState);
				break;
			case '3':
				StateStack.Pop();
				StateStack.Push(*LoadState);
				break;
			case '4' :
				for(int i = 0; i <= 5; ++i)
					StateStack.Push(*MenuState);
				break;
			default:
				for(int i = 0; i <=5; ++i)
					StateStack.Pop();
		}
		if(cInput == 'Q')
			break;
	
	}

	cin.get();

	delete GameState;
	delete MenuState;
	delete LoadState;

	return 0;
}