import pygame
import color
import random
# pygame.init()

# screen_width, screen_height = 800, 600
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption('collidelist Example')

# obstacles = [ 
#     pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
#     pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
#     pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
#     pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
#     pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
#     pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
#     pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
#     pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
#     pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
#     pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
#     pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
#     pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
#     pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
#     pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
#     pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
#     pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
#     pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
#     pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
#     pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
#     pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
#     pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
#     pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
#     pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
#     pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
#     pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
#     pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
#     pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
#     pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
#     pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
#     pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
#     pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
#     pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
#     pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
#     pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
#     pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
#     pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
#     pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
#     pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
#     pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150)),
#     pygame.Rect(random.randint(0,799),random.randint(0, 599), random.randint(50,150), random.randint(50,150))
# ]

# moving_rect = pygame.Rect(0, 0, 4, 4)

# speed = 300
# clock = pygame.time.Clock()
# ## <<--- 메인 루프
# running = True

# # 2. Event Handling & Image creation
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
            
#     # 이전 위치 저장
#     previous_position = moving_rect.topleft
#     dt = clock.tick(60) / 1000.0
    
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT]:
#         moving_rect.x -= speed * dt
#     if keys[pygame.K_RIGHT]:
#         moving_rect.x += speed * dt
#     if keys[pygame.K_UP]:
#         moving_rect.y -= speed * dt
#     if keys[pygame.K_DOWN]:
#         moving_rect.y += speed * dt
    
#     # 충돌 감지
#     collision_index = moving_rect.collidelist(obstacles)
#     if collision_index != -1:
#         print(f"{collision_index}")
        
#         moving_rect.topleft = previous_position    
        
#     screen.fill((255,255,255))
    
#     # 장애물 그리기
#     for obs in obstacles:
#         pygame.draw.rect(screen, color.rand, obs)
        
#     pygame.draw.rect(screen, color.red, moving_rect)
    
#     pygame.display.flip()
# # 3. Termination
# pygame.quit()

# 
    
import pygame

pygame.init()

# 여러 개의 Rect 객체를 생성
# (x, y, width, height)
obstacles = [
    pygame.Rect(350, 150, 100, 100),  # 첫 번째 장애물: (150, 100) 위치, 100x100 크기
    pygame.Rect(300, 300, 150, 50),   # 두 번째 장애물: (300, 300) 위치, 150x50 크기
    pygame.Rect(500, 200, 50, 150),   # 세 번째 장애물: (500, 200) 위치, 50x150 크기
    pygame.Rect(400, 400, 200, 50)    # 네 번째 장애물: (400, 400) 위치, 200x50 크기
]

# 충돌 감지를 수행할 대상 Rect 객체 생성: 파란색
moving_rect = pygame.Rect(420, 220, 100, 100)  # (420, 220) 위치, 100x100 크기

# moving_rect가 obstacles 리스트의 어떤 Rect와 충돌하는지 확인
# collidelistall 메서드는 충돌한 모든 Rect의 인덱스를 리스트로 반환.
# 충돌이 없으면 빈 리스트를 반환한다
collision_indices = moving_rect.collidelistall(obstacles)

if collision_indices:
    # 충돌이 발생한 경우, 충돌한 모든 Rect의 인덱스를 출력
    print(f"moving_rect가 obstacles[{collision_indices}]와 충돌했습니다.")
else:
    # 충돌이 발생하지 않은 경우, 해당 메시지를 출력
    print("충돌이 없습니다.")
    
    

screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
running = True
colors = [(255, 0, 0), (0, 0, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255)] # 빨간색, 검정색, 노란색, 녹색, 파란색

while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    for index, rect in enumerate(obstacles, 0):
        pygame.draw.rect(screen, colors[index],rect)
        
    pygame.draw.rect(screen, (0, 0, 255),moving_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
