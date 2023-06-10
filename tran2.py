import pygame
import sys

# Pygame 초기화
pygame.init()

# 화면 크기
화면_너비 = 800
화면_높이 = 600

# 색상
검정 = (0, 0, 0)
흰색 = (255, 255, 255)
초록 = (0, 255, 0)
빨강 = (255, 0, 0)

# 게임 창 생성
화면 = pygame.display.set_mode((화면_너비, 화면_높이))
pygame.display.set_caption("게임 제목")

# 게임 상태
타이틀_화면 = 0
메뉴_화면 = 1
인게임_화면 = 2
게임오버_화면 = 3

현재_화면 = 타이틀_화면

def 타이틀_화면_출력():
    # 타이틀 화면 출력
    화면.fill(검정)
    타이틀_폰트 = pygame.font.SysFont("malgungothicsemilight", 60)
    타이틀_텍스트 = 타이틀_폰트.render("게임 제목", True, 흰색)
    화면.blit(타이틀_텍스트, (화면_너비 // 2 - 타이틀_텍스트.get_width() // 2, 200))
    pygame.display.flip()

def 메뉴_화면_출력():
    # 메뉴 화면 출력
    화면.fill(검정)
    메뉴_폰트 = pygame.font.SysFont("malgungothicsemilight", 30)
    메뉴_텍스트 = 메뉴_폰트.render("스페이스바를 눌러 시작하세요", True, 흰색)
    화면.blit(메뉴_텍스트, (화면_너비 // 2 - 메뉴_텍스트.get_width() // 2, 300))
    pygame.display.flip()

def 인게임_화면_출력():
    # 인게임 화면 출력
    화면.fill(검정)
    인게임_폰트 = pygame.font.SysFont("malgungothicsemilight", 30)
    인게임_텍스트 = 인게임_폰트.render("인게임 화면", True, 초록)
    화면.blit(인게임_텍스트, (화면_너비 // 2 - 인게임_텍스트.get_width() // 2, 300))
    
    # 게임 요소 추가
    플레이어 = pygame.Rect(350, 450, 100, 50)
    pygame.draw.rect(화면, 빨강, 플레이어)
    
    pygame.display.flip()

def 게임오버_화면_출력():
    # 게임 오버 화면 출력
    화면.fill(검정)
    게임오버_폰트 = pygame.font.SysFont("malgungothicsemilight", 30)
    게임오버_텍스트 = 게임오버_폰트.render("게임 오버", True, 빨강)
    화면.blit(게임오버_텍스트, (화면_너비 // 2 - 게임오버_텍스트.get_width() // 2, 300))
    pygame.display.flip()

# 게임 루프
진행중 = True
while 진행중:
    for 이벤트 in pygame.event.get():
        if 이벤트.type == pygame.QUIT:
            진행중 = False
        
        if 이벤트.type == pygame.KEYDOWN:
            if 현재_화면 == 타이틀_화면:
                현재_화면 = 메뉴_화면
            elif 현재_화면 == 메뉴_화면 and 이벤트.key == pygame.K_SPACE:
                현재_화면 = 인게임_화면
            elif 현재_화면 == 인게임_화면:
                # 게임 로직 추가
                if 이벤트.key == pygame.K_LEFT:
                    플레이어.x -= 10
                elif 이벤트.key == pygame.K_RIGHT:
                    플레이어.x += 10
            elif 현재_화면 == 게임오버_화면:
                if 이벤트.key == pygame.K_SPACE:
                    현재_화면 = 타이틀_화면
    
    # 현재 화면 렌더링
    if 현재_화면 == 타이틀_화면:
        타이틀_화면_출력()
    elif 현재_화면 == 메뉴_화면:
        메뉴_화면_출력()
    elif 현재_화면 == 인게임_화면:
        인게임_화면_출력()
    elif 현재_화면 == 게임오버_화면:
        게임오버_화면_출력()

# Pygame 종료
pygame.quit()
sys.exit()
