#ifndef _SPRITE_H_
#define _SPRITE_H_

#include "glm.hpp"
//#include "Python/PythonManager.h"

class PythonManager;

using glm::vec2;

struct Sprite
{
	unsigned int m_uiSpriteID;
	char * m_pTexturePath;
	int m_iWidth;
	int m_iHeight;
	vec2 m_v2Pos;
	vec2 m_v2Vel;

	inline unsigned int ID() { return this->m_uiSpriteID; }
	inline vec2 GetPos() { return this->m_v2Pos; }
	inline vec2 GetVel() { return this->m_v2Vel; }
	inline void SetPos( float _x, float _y) { this->m_v2Pos.x = _x; this->m_v2Pos.y = _y; }
	inline void SetVel( float _x, float _y) { this->m_v2Vel.x = _x; this->m_v2Vel.y = _y; }

	void Update(PythonManager& a_PyMan );

	Sprite(char * a_pTexturePath, int a_iWidth, int a_iHeight)
		:	m_pTexturePath(a_pTexturePath), 
			m_iWidth(a_iWidth),
			m_iHeight(a_iHeight),
			m_uiSpriteID( CreateSprite(a_pTexturePath, a_iWidth, a_iHeight))
	{ }

};


#endif