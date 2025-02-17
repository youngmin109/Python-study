# import random
# import pygame

# pygame.init()

# screen_width = 800
# screen_height = 600
# screen = pygame.display.set_mode((screen_width, screen_height))
# clock = pygame.time.Clock()
# running = True

# # 게임 변수
# fall_rect_width = 80
# fall_rect_height = 40
# moving_rect_width = 50
# moving_rect_height = 40

# # 움직이는 사각형
# mov_rect_x = screen_width // 2 - moving_rect_width // 2
# mov_rect_y = screen_height - moving_rect_height - 5
# moving_rect = pygame.Rect(mov_rect_x, mov_rect_y, moving_rect_width, moving_rect_height)

# # 떨어지는 사각형 -> 3개
# fall_rect_list = []

# def generate_falling_rect():
#     for _ in range(random.randint(2, 6)):
#         while True:
#             rect_x = random.randint(0, screen_width - fall_rect_width) # 0 <= x <= 720
#             rect = pygame.Rect(rect_x, 0, fall_rect_width, fall_rect_height)
            
#             # 충돌이 발생하지 않았을 경우
#             if rect.collidelist(fall_rect_list) == -1:
#                 # 사각형을 리스트에 추가
#                 fall_rect_list.append(rect)
#                 break
    

# # 객체 이동 속도
# speed = 100 # 100 pixel / second

# # 사용자 정의 이벤트 생성
# # MY_EVENT는 pygame.USEREVENT에 1을 더하여 고유한 이벤트로 정의
# MY_EVENT = pygame.USEREVENT + 1

# # 타이머 설정: 2초마다 MY_EVENT는 이벤트가 발생하도록 설정
# pygame.time.set_timer(MY_EVENT, 2000)  # 2000밀리초(2초)마다 이벤트 발생


# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == MY_EVENT:
#             generate_falling_rect()

#     dt = clock.tick(60) / 1000  
    
#     # 사각형의 y축 좌표 증가 (위에서 아래로 이동)
#     for rect in fall_rect_list:
#         rect.y += speed * dt
        
#     # 플레이어 사각형 움직임 처리
#     keys = pygame.key.get_pressed()
    
#     # 왼쪽 방향키가 눌러졌을 때
#     if keys[pygame.K_LEFT]:
#         moving_rect.x -= speed * dt      

#     # 오른쪽 방향키가 눌러졌을 때
#     if keys[pygame.K_RIGHT]:
#         moving_rect.x += speed * dt 
            
#     # 충돌 감지
#     if moving_rect.collidelist(fall_rect_list) != -1:
#         print("충돌 발생, 게임 종료")
#         running = False
        
#     # 화면 아래이면 리스트에 삭제
#     for rect in fall_rect_list[:]:
#         if rect.y > screen_height:
#             fall_rect_list.remove(rect)
    
#     # 화면 그리기
#     screen.fill((255, 255, 255))
    
#     # 떨어지는 사각형
#     for rect in fall_rect_list:    
#         pygame.draw.rect(screen, (0, 0, 255), rect)
        
#     # 플레이어 사각형
#     pygame.draw.rect(screen, (255, 0, 0), moving_rect)
        
#     # 지금까지 메모리에 작성된 그림을 화면(Screen)에 출력
#     pygame.display.flip()
    
#     print(len(fall_rect_list))
        
# pygame.quit()


# # # Pygame 초기화
# # # Pygame 초기화
# import pygame
# import random

# # Pygame 초기화
# pygame.init()

# # 화면 설정
# screen_width, screen_height = 800, 600
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption('Falling Squares')

# # 색상 정의
# WHITE = (255, 255, 255)  # 배경 색상
# BLACK = (0, 0, 0)  # 텍스트 색상
# RED = (255, 0, 0)  # 플레이어 색상
# BLUE = (0, 0, 255)  # 떨어지는 사각형 색상

# # 폰트 설정 (크기 36)
# font = pygame.font.Font(None, 36)

# # 사용자 정의 이벤트 설정
# SPAWN_SQUARE = pygame.USEREVENT + 1
# pygame.time.set_timer(SPAWN_SQUARE, 1000)  # 1초마다 사각형 생성 이벤트 발생

# # 게임 변수 초기화
# player_width = 50
# player_height = 50
# player_speed = 300  # 플레이어 이동 속도 (초당 300 픽셀)
# player = pygame.Rect(
#     (screen_width - player_width) // 2, 
#     screen_height - player_height - 10, 
#     player_width, 
#     player_height
# )  # 플레이어 사각형 생성 (화면 하단 중앙)

# falling_squares = []  # 떨어지는 사각형 리스트
# falling_speed = 200  # 떨어지는 사각형 속도 (초당 200 픽셀)

# f_rect_width = 15
# f_rect_height = 15
# fire_speed = 300

# # 총알 사각형을 보관할 리스트 생성
# f_rect_list = []


# start_time = pygame.time.get_ticks()  # 게임 시작 시간
# game_duration = 30  # 게임 지속 시간 30초

# # FPS 제어를 위한 Clock 객체 생성
# clock = pygame.time.Clock()

# # 게임 루프
# running = True
# while running:
#     # 델타 타임 계산 (초 단위 경과 시간)
#     dt = clock.tick(60) / 1000.0  # 60 FPS로 제한

#     # 이벤트 처리
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:  # 창 닫기 버튼을 누르면 게임 종료
#             running = False
#         elif event.type == SPAWN_SQUARE:  # 사각형 생성 이벤트 발생 시
#             # 여러 개의 새로운 사각형을 랜덤 위치에 추가
#             for _ in range(random.randint(1, 5)):  # 1~5개의 사각형 생성
#                 x_position = random.randint(0, screen_width - player_width)  # 화면 내 랜덤 X 위치
#                 new_square = pygame.Rect(x_position, 0, player_width, player_height)
#                 falling_squares.append(new_square)  # 새로운 사각형 리스트에 추가
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_SPACE:
#                 fire_rect = pygame.Rect(0, 0, f_rect_width, f_rect_height)
#                 # 생성된 사각형을 플레이어 사각형 Top 중앙에 위치
#                 fire_rect.bottom = player.top
#                 fire_rect.x = player.centerx - f_rect_width // 2
#                 # 생성된 총알 사각형을 리스트에 추가
#                 f_rect_list.append(fire_rect)


#     # 키 입력 처리
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT] and player.left > 0:  # 왼쪽 화살표 키로 플레이어 이동
#         player.x -= player_speed * dt  # 델타 타임을 사용하여 프레임 독립적 이동
#     if keys[pygame.K_RIGHT] and player.right < screen_width:  # 오른쪽 화살표 키로 플레이어 이동
#         player.x += player_speed * dt  # 델타 타임을 사용하여 프레임 독립적 이동

#     # 총알 이동 처리
#     for f_rect in f_rect_list[:]:
#         f_rect.y -= fire_speed * dt
#         if f_rect.y < 0:
#             f_rect_list.remove(f_rect)
            
#     # 떨어지는 사각형 이동 및 충돌 체크
#     for square in falling_squares[:]:  # 리스트 복사본을 사용하여 반복
#         square.y += falling_speed * dt  # 델타 타임을 사용한 이동
#         if square.colliderect(player):  # 플레이어와 충돌 시
#             print("충돌! 게임 종료")
#             running = False  # 게임 종료
#         if square.top > screen_height:  # 화면을 벗어난 사각형 제거
#             falling_squares.remove(square)
            
#     # 총알과 떨어지는 사각형 충돌 체크
#     for f_rect in f_rect_list[:]:
#         # 리스트로부터 총알 사각형 가지고 오기
#         is_collision = False
         
#         for fr_rect in falling_squares[:]:
#             if f_rect.colliderect(fr_rect):
#                 falling_squares.remove(fr_rect)
#                 is_collision = True
        
#         if is_collision:
#             f_rect_list.remove(f_rect)

#     # 경과 시간 계산
#     elapsed_time = (pygame.time.get_ticks() - start_time) / 1000  # 초 단위로 변환

#     # 게임 승리 조건 체크
#     if elapsed_time >= game_duration:
#         print("30초 동안 생존! 승리!")
#         running = False  # 게임 종료

#     # 화면 초기화
#     screen.fill(WHITE)

#     # 경과 시간 텍스트 생성 및 화면 출력
#     timer_text = font.render(f"Time: {elapsed_time:.2f} seconds", True, BLACK)
#     screen.blit(timer_text, (10, 10))  # 텍스트를 화면 왼쪽 상단에 출력

#     # 사각형 그리기
#     pygame.draw.rect(screen, RED, player)  # 플레이어 사각형 그리기
#     for square in falling_squares:
#         pygame.draw.rect(screen, BLUE, square)  # 떨어지는 사각형 그리기

#     # 총알 그리기
#     for f_rect in f_rect_list:
#         pygame.draw.rect(screen, (0, 255, 0), f_rect) 
        
#     # 화면 업데이트
#     pygame.display.flip()

# # 게임 종료
# pygame.quit()



bar = [1,2,3,4]
for i in bar:
    bar.remove(i)
print(bar)