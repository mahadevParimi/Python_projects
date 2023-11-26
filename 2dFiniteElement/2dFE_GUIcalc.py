import numpy as np
import customtkinter as ctk
from PIL import Image,ImageTk,ImageFont,ImageDraw

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

def calc():

    e1 =  float(e1_text.get(0.0, 'end'))
    e2 =  float(e2_text.get(0.0, 'end'))
    a1  = float(a1_text.get(0.0, 'end'))
    a2  = float(a2_text.get(0.0, 'end'))
    l1  = float(l1_text.get(0.0, 'end'))
    l2  = float(l2_text.get(0.0, 'end'))
    f1x = float(f1x_text.get(0.0, 'end'))
    f2x = float(f2x_text.get(0.0, 'end'))
    f3x = float(f3x_text.get(0.0, 'end'))

    img = Image.open("pranshu/images.jpg")
    font = ImageFont.truetype("pranshu/times new roman bold italic.ttf",22)
    draw = ImageDraw.Draw(img)
    draw.text((100,50+10),f"E1 = {e1} psi",(0,0,0),font=font)
    draw.text((340,50+10),f"E2 = {e2} psi",(0,0,0),font=font)
    draw.text((100,80+10),f"A1 = {a1} in²",(0,0,0),font=font)
    draw.text((340,80+10),f"A2 = {a2} in²",(0,0,0),font=font)
    draw.text((150,175),f"{l1} in",(0,0,0),font=font)
    draw.text((390,175),f"{l2} in",(0,0,0),font=font)
    draw.text((590,90),f"{f3x} lb",(0,0,0),font=font)

    img_resize = ctk.CTkImage(light_image=img,size=(500,170))
    img_label = ctk.CTkLabel(window,image=img_resize)
    img_label.place(x=refx+10,y=refy+4*gapy)

    ae1_l,ae2_l = a1*e1/l1 ,a2*e2/l2

    stiff_123 = [
                [ae1_l+ae2_l,  -ae2_l],
                [-ae2_l,  ae2_l]
                ]

    f_mat = [[f2x],[f3x]]
    f_mat =  np.array(f_mat)
    stiff_123 = np.array(stiff_123)
    stiff_123_inv = np.linalg.inv(stiff_123)
    d_mat = np.matmul(stiff_123_inv,f_mat)
    d1x, d2x, d3x = 0, d_mat[0][0], d_mat[1][0]
    e1x, e2x = (d2x-d1x)/l1, (d3x-d2x)/l2
    s1x, s2x = e1*e1x, e2*e2x
    f12x, f23x = ae1_l*(d1x-d2x), ae2_l*(d2x-d3x)
    f21x, f32x = -f12x , -f23x

    displacements =f"\nDisplacements: \n\td1x = {d1x:0.3f} inch\n\td2x = {d2x} inch \n\td3x = {d3x} inch\n"
    strains =f"Strains: \n\te1x = {e1x}\n\te2x = {e2x}\n"
    stress =f"Stress: \n\t𝝈1x = {s1x}\n\t𝝈2x = {s2x}\n"
    forces =f"Element Forces: \n\tF¹1x = {f12x}\n\tF¹2x = {f21x}\n\n\tF²2x = {f23x}\n\tF²3x = {f32x}\n"
    output = displacements + strains + stress + forces

    disp_text.insert(0.0,output)

width,height= 540,750
size = 60
ll,ul=180,0
refx,refy=10,30
gapx,gapy=170,50
gapx1,gapy1=1,200
disp_w,disp_h=130,20
slider_w,slider_h = 25,450

window = ctk.CTk()
window.title("GROUP-5")
window.resizable(False,False)
window.geometry(f"{width}x{height}")

e1_label = ctk.CTkLabel(window,text="E1 : ")
e1_label.place(x=refx,y=refy)
e1_text = ctk.CTkTextbox(window,width=disp_w,height=disp_h,activate_scrollbars=False)
e1_text.place(x=refx+30,y=refy)
e1_text.insert(0.0,"0")

e2_label = ctk.CTkLabel(window,text="E2 : ")
e2_label.place(x=refx+gapx,y=refy)
e2_text = ctk.CTkTextbox(window,width=disp_w,height=disp_h,activate_scrollbars=False)
e2_text.place(x=refx+30+gapx,y=refy)
e2_text.insert(0.0,"0")

a1_label = ctk.CTkLabel(window,text="A1 :  ")
a1_label.place(x=refx+2*gapx+10,y=refy)
a1_text = ctk.CTkTextbox(window,width=disp_w,height=disp_h,activate_scrollbars=False)
a1_text.place(x=refx+40+2*gapx,y=refy)
a1_text.insert(0.0,"0")

a2_label = ctk.CTkLabel(window,text="A2 :  ")
a2_label.place(x=refx+2*gapx+10,y=refy+gapy)
a2_text = ctk.CTkTextbox(window,width=disp_w,height=disp_h,activate_scrollbars=False)
a2_text.place(x=refx+40+2*gapx,y=refy+gapy)
a2_text.insert(0.0,"0")

f1x_label = ctk.CTkLabel(window,text="F1 : ")
f1x_label.place(x=refx,y=refy+2*gapy)
f1x_text = ctk.CTkTextbox(window,width=disp_w,height=disp_h,activate_scrollbars=False)
f1x_text.place(x=refx+30,y=refy+2*gapy)
f1x_text.insert(0.0,"0")

f2x_label = ctk.CTkLabel(window,text="F2 : ")
f2x_label.place(x=refx+gapx,y=refy+2*gapy)
f2x_text = ctk.CTkTextbox(window,width=disp_w,height=disp_h,activate_scrollbars=False)
f2x_text.place(x=refx+30+gapx,y=refy+2*gapy)
f2x_text.insert(0.0,"0")

f3x_label = ctk.CTkLabel(window,text="F3 : ")
f3x_label.place(x=refx+2*gapx+10,y=refy+2*gapy)
f3x_text = ctk.CTkTextbox(window,width=disp_w,height=disp_h,activate_scrollbars=False)
f3x_text.place(x=refx+40+2*gapx,y=refy+2*gapy)
f3x_text.insert(0.0,"0")

l1_label = ctk.CTkLabel(window,text="L1 : ")
l1_label.place(x=refx,y=refy+gapy)
l1_text = ctk.CTkTextbox(window,width=disp_w,height=disp_h,activate_scrollbars=False)
l1_text.place(x=refx+30,y=refy+gapy)
l1_text.insert(0.0,"0")

l2_label = ctk.CTkLabel(window,text="L2: ")
l2_label.place(x=refx+gapx,y=refy+gapy)
l2_text = ctk.CTkTextbox(window,width=disp_w,height=disp_h,activate_scrollbars=False)
l2_text.place(x=refx+55+145,y=refy+gapy)
l2_text.insert(0.0,"0")

disp_text = ctk.CTkTextbox(window,width=disp_w*4-20,height=disp_h*15,activate_scrollbars=False)
disp_text.place(x=refx+10,y=refy+8*gapy-10)

calc_btn = ctk.CTkButton(window,text="CALCULATE",command=calc,hover_color="green")
calc_btn.place(x=refx+55+140,y=refy+3*gapy)

window.mainloop()