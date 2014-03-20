#ifndef _STACK_H_
#define _STACK_H_

/* 
	Currently functions completely fine. However if I push like a million states eventually it corrupts the heap.
*/
template <class T>
class Stack
{
	private:

		T * m_paData; 
		unsigned int m_uiSize; 
		int m_iTop; 
		unsigned int m_uiGrowSize; 

	public:

		Stack(unsigned int a_uiSize, unsigned int a_uiGrowSize = 1);
		~Stack();
		bool Empty() const;
		bool Full() const;
		int GetSize() const;
		void Push(T &a_roValue);
		void Pop();
		const T* Top();
		void UpdateAll(void (*ClassCallback)(const T*));
};

#include "Stack.inl"

#endif

