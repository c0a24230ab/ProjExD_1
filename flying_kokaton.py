import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600)) #練習１
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    kk_img = pg.image.load("fig/3.png") #練習２
    kk_img = pg.transform.flip(kk_img, True, False)# 練習８
    bg_img_flip = pg.transform.flip(bg_img, True,False)
    tmr = 0

    kk_rct = kk_img.get_rect() #練習１０ー１
    kk_rct.center = 300,200 #練習１０－２   

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return #練習３

        x = tmr%3200  #練習６
        screen.blit(bg_img,[-x, 0])
        screen.blit(bg_img_flip,[-x+1600,0]) #練習７
        screen.blit(bg_img,[-x+3200,0])
        
        x = -1
        y = 0

        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            x = 0
            y = -1

        if key_lst[pg.K_DOWN]:
            x = 0
            y = 1

        if key_lst[pg.K_LEFT]:
            x = -1
            y = 0


        if key_lst[pg.K_RIGHT]:
            x = 1
            y = 0

        screen.blit(kk_img,kk_rct) #練習４

        kk_rct.move_ip((x,y))
        
        pg.display.update()
        tmr += 1
        clock.tick(200) #練習５



if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
