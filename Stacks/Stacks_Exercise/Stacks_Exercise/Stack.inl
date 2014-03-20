#include "Stack.h"

template<class T>
Stack<T>::Stack(unsigned int a_uiSize, unsigned int a_uiGrowSize) : 
	m_paData(NULL),
	m_uiSize(a_uiSize),
	m_uiGrowSize(a_uiGrowSize),
	m_iTop(-1)
{
	if(m_uiSize)
	{
		m_paData = new T[m_uiSize];
		memset(m_paData, 0 , sizeof(T) * m_uiSize);
	}
}

template<class T>
Stack<T>::~Stack()
{
	if(m_paData != NULL)
	{
		delete[] m_paData;
		m_paData = NULL;
	}
}


template<class T>
bool Stack<T>::Empty() const
{
	return (m_iTop == -1) ? true : false;
}

template<class T>
bool Stack<T>::Full() const
{
	if(sizeof(m_paData) >= sizeof(T) * m_uiSize)
			return true;
		else
			return false;
}

template<class T>
int Stack<T>::GetSize() const
{
	return (m_iTop + 1);
}

template<class T>
void Stack<T>::Push(T &a_roValue)
{
	m_iTop++;
	
	if(m_iTop >= m_uiSize)
	{
		int iNewSize = m_uiSize + m_uiGrowSize; // Size for new array

		T * pNewData = new T[iNewSize]; // Dynamic allocation for new array
		memset(pNewData, 0, sizeof(T) * iNewSize); //Initialize all blocks of memory in new array to 0
		T * pOldData = m_paData; //Store current array data into a temporary pointer
		memset(pOldData, 0, sizeof(T) * m_uiSize);

		for(int i = 0 ; i < (int)m_uiSize; ++i) //Copy objects from current array into new array
			pNewData[i] = m_paData[i];

		m_paData = pNewData; //Change address of current array to new array

		m_uiSize = iNewSize; //Array is now m_uiGrowSize blocks larger

		delete[] pOldData; //Clean up old temp array
	}
	
	m_paData[ m_iTop ] = a_roValue; //Push new object on top of the stack
}

template<class T>
void Stack<T>::Pop()
{
	if(Empty())
		return;

	m_iTop--;
	
	if(m_iTop <= m_uiSize)
	{
		int iNewSize = m_uiSize - m_uiGrowSize; // Size for new array

		T * pNewData = new T[iNewSize]; // Dynamic allocation for new array
		memset(pNewData, 0, sizeof(T) * iNewSize); //Initialize all blocks of memory in new array to 0
		T * pOldData = m_paData; //Store current array data into a temporary pointer
		memset(pOldData, 0, sizeof(T) * m_uiSize);

		for(int i = 0 ; i < (int)iNewSize; ++i) //Copy objects from current array into new array
			pNewData[i] = m_paData[i];

		m_paData = pNewData; //Change address of current array to new array

		m_uiSize = iNewSize; //Array is now m_uiGrowSize blocks larger

		delete[] pOldData; //Clean up old temp array
	}
}


template<class T>
const T* Stack<T>::Top()
{
	return &m_paData[m_iTop];
}

template<class T>
void Stack<T>::UpdateAll(void (*ClassCallback)(const T*))
{
	T * pEnd = m_paData + m_iTop; 
	for(T * p = pEnd; p >= m_paData; --p)
	{
		ClassCallback(p);
	}
}