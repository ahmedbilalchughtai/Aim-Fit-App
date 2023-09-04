screenss = """
ScreenManager:
    Login:
    Account:
    Main:
    About:
    Bmi:
    Exercise:
    UnderWeightScreen:
    NormalWeightScreen:
    OverWeightScreen:
<Login>:
    name: "login"
    email: email
    password: password
    
    Image: 
        source : 'aimfit1.png'
        pos_hint : {'center_x' : 0.5, 'center_y' : 0.7}
        size_hint : 0.5, 0.3
        
    MDTextField:
        id : email
        hint_text : "Enter Email"
        helper_text : "or click on Make New Account to create one"
        helper_text_mode : "on_focus"
        icon_right : "account-lock"
        icon_right_color : app.theme_cls.primary_color
        pos_hint : {"center_x" : 0.5, "center_y" : 0.5 }
        size_hint_x : None
        width : 300
        
    MDTextField:
        id : password
        hint_text : "Enter Password"
        helper_text  : "or click on Make New Account to create one"
        helper_text_mode : "on_focus"
        icon_right : 'lock'
        icon_right_color : app.theme_cls.primary_color
        pos_hint : {'center_x' : 0.5, 'center_y' : 0.4}
        size_hint_x : None
        width : 300
        
    MDRectangleFlatButton:
        text : '              Login              '
        pos_hint :{'center_x' : 0.5, 'center_y' : 0.25}
        on_press:
            root.manager.transition.direction = "up"
            root.loginBtn()    
                      
    MDRectangleFlatButton:
        text : 'Make New Account'
        pos_hint :{'center_x' : 0.5, 'center_y' : 0.15}
        on_press:
            root.manager.current = 'account'
            root.manager.transition.direction = "left"
    
        
<Account>:
    name : "account"
    
    namee: namee
    email: email
    password: passw
    
    Image: 
        source : 'aimfit1.png'
        pos_hint : {'center_x' : 0.5, 'center_y' : 0.7}
        size_hint : 0.5, 0.3
    MDTextField:
        id : namee
        hint_text : "Name"
        pos_hint : {"center_x" : 0.5, "center_y" : 0.5 }
        size_hint_x : None
        width : 300    
    MDTextField:
        id : email
        hint_text : "Email"
        pos_hint : {"center_x" : 0.5, "center_y" : 0.4 }
        size_hint_x : None
        width : 300    
    MDTextField:
        id : passw
        hint_text : "Password"
        pos_hint : {"center_x" : 0.5, "center_y" : 0.3 }
        size_hint_x : None
        width : 300
    MDRectangleFlatButton:
        text : 'Done'
        pos_hint: {'center_x': 0.5, 'center_y' : 0.2}
        on_press: 
            root.manager.transition.direction = "right"
            root.submit()
    MDRectangleFlatButton:
        text : 'Back'
        pos_hint: {'center_x': 0.5, 'center_y' : 0.1}
        on_press: 
            root.manager.transition.direction = "right"
            root.manager.current = 'login'        
     
<Main>:
    name : "aim"
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation : "vertical"
                    MDToolbar:
                        title : "AimFit"
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                    Widget:
                Image:
                    source : 'aimfit2.png'
                    pos_hint : {'center_x' : 0.5, 'center_y' : 0.55}
                    size_hint : 1 , 0.7
                        
                MDRectangleFlatButton:
                    text : 'Lets get Started!'
                    pos_hint : {'center_x' : 0.5 , 'center_y' : 0.2}
                    on_press : 
                        root.manager.current  = "bmi"
                        root.manager.transition.direction = "left"
                    
                MDBottomAppBar:
                    MDToolbar:
                        mode: "end"
                        type: "bottom"
                        icon: "home"
                        on_action_button: 
                            root.manager.current = 'aim'     

        MDNavigationDrawer:
            id : nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing : '8dp'
                padding : '8dp'
                Image:
                    source: 'aimfit2.png'
                    
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'AimFit'
                            IconLeftWidget:
                                icon : 'home'
                        OneLineIconListItem:
                            text: 'About Us'
                            on_press:     
                                root.manager.current = 'about'
                                root.manager.transition.direction = "up"
                            IconLeftWidget:
                                icon : 'face-profile'
                                on_press:     
                                    root.manager.current = 'about'
                                    root.manager.transition.direction = "up"
                        OneLineIconListItem:
                            text: 'Exercise Plan'
                            on_press:
                                root.manager.current = 'exercise' 
                                root.manager.transition.direction = "up"
                            IconLeftWidget:
                                icon : 'weight-lifter'
                                on_press:     
                                    root.manager.current = 'exercise'
                                    root.manager.transition.direction = "up"                                    
                        OneLineIconListItem:
                            text: 'Logout'
                            on_press:
                                root.manager.current = 'login' 
                                root.manager.transition.direction = "down"
                            IconLeftWidget:
                                icon : 'logout'
                                on_press:     
                                    root.manager.current = 'login'
                                    root.manager.transition.direction = "down"
<About>:
    name : 'about'
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation : "vertical"
                    MDToolbar:
                        title : "AimFit"
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                        elevation: 10
                    
                Image:
                    source : 'aimfit1.png'
                    pos_hint : {'center_x' : 0.35 , 'center_y' : 0.8}
                    size_hint :  0.5 , 0.3 
                Image:
                    source : 'istlogo.png'
                    pos_hint : {'center_x' : 0.67 , 'center_y' : 0.8}
                    size_hint :  0.2 , 0.2    
                MDLabel:
                    text : "About Us"
                    font_style:'H3'
                    pos_hint : {'center_x' : 0.5 ,'center_y' : 0.6}
                    halign : 'center'
                    valign : 'middle'
                    theme_text_color : 'Custom'
                    text_color : 1,1,0,1
                MDLabel:
                    text : "A Object Oriented Programming project on Python that is bacially a fitness application that provides us the guidness towards our health and body state"
                    font_style:'Subtitle1'
                    pos_hint : {'center_x' : 0.5 ,'center_y' : 0.5}
                    halign : 'center'
                    valign : 'middle'
                MDLabel:
                    text : "Project by"
                    font_style:'H3'
                    pos_hint : {'center_x' : 0.5 ,'center_y' : 0.355}
                    halign : 'center'
                    valign : 'middle'
                    theme_text_color : 'Custom'
                    text_color : 1,1,0,1
                MDLabel:
                    text: " Muhammad Haseeb (210201057) , Riffah Eman (210201025) , Ibraheem Lughmani (210201044) , Abdul Rafay Amir (210201019) , Ahmed Bilal (210201096)"
                    font_style:'Subtitle1'
                    pos_hint : {'center_x' : 0.5 ,'center_y' : 0.2}
                    halign : 'center'
                    valign : 'middle'       
                MDBottomAppBar:
                    MDToolbar:
                        mode: "end"
                        type: "bottom"
                        icon: "home"
                        on_action_button: 
                            root.manager.current = 'aim'
                            root.manager.transition.direction = "up"      

        MDNavigationDrawer:
            id : nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing : '8dp'
                padding : '8dp'
                Image:
                    source: 'aimfit2.png'
                    
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'AimFit'
                            on_press:     
                                root.manager.current = 'aim'
                                root.manager.transition.direction = "down"
                            IconLeftWidget:
                                icon : 'home'
                                on_press:     
                                    root.manager.current = 'aim'
                                    root.manager.transition.direction = "down"
                        OneLineIconListItem:
                            text: 'About Us'
                            IconLeftWidget:
                                icon : 'face-profile'
                        OneLineIconListItem:
                            text: 'Exercise Plan'
                            on_press:
                                root.manager.current = 'exercise' 
                                root.manager.transition.direction = "up"
                            IconLeftWidget:
                                icon : 'weight-lifter'
                                on_press:     
                                    root.manager.current = 'exercise'
                                    root.manager.transition.direction = "up"         
                        OneLineIconListItem:
                            text: 'Logout'
                            on_press:
                                root.manager.current = 'login' 
                                root.manager.transition.direction = "down"
                            IconLeftWidget:
                                icon : 'logout'
                                on_press:     
                                    root.manager.current = 'login'
                                    root.manager.transition.direction = "down"
<Bmi>:
    name: 'bmi'
    
    weight: weight
    h: h
    ttttext : ttttext
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation : "vertical"
                    MDToolbar:
                        title : "AimFit"
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                        elevation: 10
                    Widget:
                
                Image: 
                    source : 'aimfit1.png'
                    pos_hint : {'center_x' : 0.5, 'center_y' : 0.75}
                    size_hint : 0.5, 0.3 
                MDLabel:
                    text : "B.M.I Calculator"
                    font_style:'H3'
                    pos_hint : {'center_x' : 0.5 ,'center_y' : 0.55}
                    halign : 'center'
                    valign : 'middle'
                    theme_text_color : 'Custom'
                    text_color : 1,1,0,1        
                MDTextField:
                    id : weight
                    hint_text : "Enter Weight"
                    helper_text : "In Kilograms"
                    helper_text_mode : "on_focus"
                    pos_hint : {"center_x" : 0.5, "center_y" : 0.4 }
                    size_hint_x : None
                    width : 300
                    
                MDTextField:
                    id : h 
                    hint_text : "Enter Height"
                    helper_text : "In Meters(1 feet = 0.3 meters)"
                    helper_text_mode : "on_focus"
                    pos_hint : {"center_x" : 0.5, "center_y" : 0.3 }
                    size_hint_x : None
                    width : 300 
                
                MDRectangleFlatButton:
                    text : 'Calculate'
                    pos_hint : {'center_x' : 0.5 , 'center_y' : 0.2}
                    on_press : 
                        root.calculate()
                        root.manager.transition.direction = "left"
                
                MDLabel:
                    id : ttttext 
                    pos_hint : {'center_x' : 0.5 ,'center_y' : 0.145}
                    halign : 'center'
                    valign : 'middle'
             
                          
                MDBottomAppBar:
                    MDToolbar:
                        mode: "end"
                        type: "bottom"
                        icon: "home"
                        on_action_button: 
                            root.manager.current = 'aim'       

        MDNavigationDrawer:
            id : nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing : '8dp'
                padding : '8dp'
                Image:
                    source: 'aimfit2.png'
                    
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'AimFit'
                            on_press:     
                                root.manager.current = 'aim'
                                root.manager.transition.direction = "down"
                            IconLeftWidget:
                                icon : 'home'
                                on_press:     
                                    root.manager.current = 'aim'
                                    root.manager.transition.direction = "down"
                        OneLineIconListItem:
                            text: 'About Us'
                            on_press:
                                root.manager.current = 'about' 
                                root.manager.transition.direction = "down"
                            IconLeftWidget:
                                icon : 'face-profile'
                                on_press:
                                    root.manager.current = 'about' 
                                    root.manager.transition.direction = "down"
                        OneLineIconListItem:
                            text: 'Exercise Plan'
                            on_press:
                                root.manager.current = 'exercise' 
                                root.manager.transition.direction = "up"
                            IconLeftWidget:
                                icon : 'weight-lifter'
                                on_press:     
                                    root.manager.current = 'exercise'
                                    root.manager.transition.direction = "up"                                     
                        OneLineIconListItem:
                            text: 'Logout'
                            on_press:
                                root.manager.current = 'login' 
                                root.manager.transition.direction = "down"
                            IconLeftWidget:
                                icon : 'logout'
                                on_press:     
                                    root.manager.current = 'login'
                                    root.manager.transition.direction = "down"
<Exercise>:
    name : 'exercise'
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation : "vertical"
                    MDToolbar:
                        title : "AimFit"
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                    Widget:
                Image:
                    source : 'aimfit1.png'
                    pos_hint : {'center_x' : 0.5, 'center_y' : 0.7}
                    size_hint : 0.5 , 0.3
                MDLabel:
                    text : "Select Category"
                    font_style:'H3'
                    pos_hint : {'center_x' : 0.5 ,'center_y' : 0.55}
                    halign : 'center'
                    valign : 'middle'
                    theme_text_color : 'Custom'
                    text_color : 1,1,0,1                    
                MDRectangleFlatButton:
                    text : '  Underweight  '
                    pos_hint : {'center_x' : 0.5 , 'center_y' : 0.45}
                    on_press : 
                        root.manager.current  = "UnderWeight"
                        root.manager.transition.direction = "left"
                MDRectangleFlatButton:
                    text : 'Normalweight'
                    pos_hint : {'center_x' : 0.5 , 'center_y' : 0.35}
                    on_press : 
                        root.manager.current  = "NormalWeight"
                        root.manager.transition.direction = "left"
                MDRectangleFlatButton:
                    text : '   Overweight   '
                    pos_hint : {'center_x' : 0.5 , 'center_y' : 0.25}
                    on_press : 
                        root.manager.current  = "OverWeight"
                        root.manager.transition.direction = "left"                             
                MDBottomAppBar:
                    MDToolbar:
                        mode: "end"
                        type: "bottom"
                        icon: "home"
                        on_action_button: 
                            root.manager.current = 'aim' 
        MDNavigationDrawer:
            id : nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing : '8dp'
                padding : '8dp'
                Image:
                    source: 'aimfit2.png'
                    
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'AimFit'
                            on_press:     
                                root.manager.current = 'aim'
                                root.manager.transition.direction = "down"
                            IconLeftWidget:
                                icon : 'home'
                                on_press:     
                                    root.manager.current = 'aim'
                                    root.manager.transition.direction = "down"
                        OneLineIconListItem:
                            text: 'About Us'
                            on_press:     
                                root.manager.current = 'about'
                                root.manager.transition.direction = "up"
                            IconLeftWidget:
                                icon : 'face-profile'
                                on_press:     
                                    root.manager.current = 'about'
                                    root.manager.transition.direction = "up"
                        OneLineIconListItem:
                            text: 'Exercise Plan'
                            IconLeftWidget:
                                icon : 'weight-lifter'                                   
                        OneLineIconListItem:
                            text: 'Logout'
                            on_press:
                                root.manager.current = 'login' 
                                root.manager.transition.direction = "down"
                            IconLeftWidget:
                                icon : 'logout'
                                on_press:     
                                    root.manager.current = 'login'
                                    root.manager.transition.direction = "down"
<UnderWeightScreen>:
    name:'UnderWeight'
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation:'vertical'  
                    MDToolbar:
                        title:'AimFit'
                        left_action_items:[["menu",lambda x:nav_drawer.set_state("open")]]
                    Widget:
                MDLabel:
                    text:'Exercises you need'
                    font_style:'H3'
                    theme_text_color:"Custom"
                    text_color:1,1,0,1
                    halign:'center'
                    valign:'middle'
                    height:self.texture_size[1] 
                    pos_hint : {'center_x':0.5 ,'center_y' : 0.85} 
                MDLabel:
                    text:'Push-ups'
                    font_style:'H4'
                    theme_text_color:'Custom'
                    halign:'center'
                    valign:'middle'
                    text_color:1,1,0,1
                    pos_hint:{'center_x':0.5,'center_y':0.75}   
                MDLabel:
                    text:'Good old push-ups should be one of the first exercises that come to your mind when you think about weight gain. This is because push-ups help you build muscles in your chest and arms. When combined with the right protein and calorie diet, push-ups can turn into a lethal weapon in your weight gain arsenal. Push-ups are very efficient when they are done to the point of hypertrophy, i.e., muscle cell growth, and this is attained by pushing your body to the limit every time you do a push-up.'
                    padding_x:20
                    theme_text_color:'Custom'
                    text_color:1,1,1,1
                    halign:'center'
                    valign:'middle'
                    pos_hint:{'center_x':0.5,'center_y':0.62}
                MDLabel:
                    text:'Deadlifts'
                    font_style:'H4'
                    theme_text_color:'Custom'
                    halign:'center'
                    valign:'middle'
                    text_color:1,1,0,1
                    pos_hint:{'center_x':0.5,'center_y':0.48}
                MDLabel:
                    text:'Deadlifts are used by fitness trainers to help their students with weight loss and fat loss, but it is also a very potent tool for people to gain weight. Because of its ability to engage the maximum number of muscles in the body, it has a reputation for being one of the most credible exercises in helping you ensure your weight gain is distributed evenly among every part of your body.'
                    padding_x:20
                    theme_text_color:'Custom'
                    text_color:1,1,1,1
                    halign:'center'
                    valign:'middle'
                    pos_hint:{'center_x':0.5,'center_y':0.35}
                MDLabel:
                    text:'Squats'
                    font_style:'H4'
                    theme_text_color:'Custom'
                    halign:'center'
                    valign:'middle'
                    text_color:1,1,0,1
                    pos_hint:{'center_x':0.5,'center_y':0.25}
                MDLabel:
                    text:'Squats are powerful tools that people, especially underweight people, can use to build their butt muscles, leg muscles, and quads. If you are involved in a lot of fitness programs for fat loss and muscle gain, you must have come across this exercise many times.' 
                    padding_x:20
                    theme_text_color:'Custom'
                    text_color:1,1,1,1
                    halign:'center'
                    valign:'middle'
                    pos_hint:{'center_x':0.5,'center_y':0.16}
                MDBottomAppBar:
                    MDToolbar:    
                        mode:'end'   
                        type:'bottom' 
                        icon:'home'
                        on_action_button:    
                            root.manager.current='aim'
        MDNavigationDrawer:
            id : nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing : '8dp'
                padding : '8dp'
                Image:
                    source: 'aimfit2.png'
                    
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'AimFit'
                            on_press:     
                                root.manager.current = 'aim'
                                root.manager.transition.direction = "down"
                            IconLeftWidget:
                                icon : 'home'
                                on_press:     
                                    root.manager.current = 'aim'
                                    root.manager.transition.direction = "down"
                        OneLineIconListItem:
                            text: 'About Us'
                            on_press:
                                root.manager.current = 'about' 
                                root.manager.transition.direction = "down"
                            IconLeftWidget:
                                icon : 'face-profile'
                                on_press:
                                    root.manager.current = 'about' 
                                    root.manager.transition.direction = "down"
                        OneLineIconListItem:
                            text: 'Exercise Plan'
                            on_press:
                                root.manager.current = 'exercise' 
                                root.manager.transition.direction = "up"
                            IconLeftWidget:
                                icon : 'weight-lifter'
                                on_press:     
                                    root.manager.current = 'exercise'
                                    root.manager.transition.direction = "up"                                     
                        OneLineIconListItem:
                            text: 'Logout'
                            on_press:
                                root.manager.current = 'login' 
                                root.manager.transition.direction = "down"
                            IconLeftWidget:
                                icon : 'logout'
                                on_press:     
                                    root.manager.current = 'login'
                                    root.manager.transition.direction = "down"
<NormalWeightScreen>:
    name:'NormalWeight'
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation:'vertical'  
                    MDToolbar:
                        title:'AimFit'
                        left_action_items:[["menu",lambda x:nav_drawer.set_state("open")]]
                    Widget:
                MDLabel:
                    text:'Exercises you need'
                    font_style:'H3'
                    theme_text_color:"Custom"
                    text_color:1,1,0,1
                    halign:'center'
                    valign:'middle'
                    height:self.texture_size[1] 
                    pos_hint : {'center_x':0.5 ,'center_y' : 0.85}    
                MDLabel:
                    text:'Dumbbell Rows'
                    font_style:'H4'
                    theme_text_color:'Custom'
                    halign:'center'
                    valign:'middle'
                    text_color:1,1,0,1
                    pos_hint:{'center_x':0.5,'center_y':0.75}                    
                MDLabel:
                    text:'The dumbbell row, also known as the bent-over dumbbell row, is a compound back exercise. Perform dumbbell rows by hinging your hips with your back straight and lifting a pair of dumbbells with a neutral grip (palms facing each other). Like other rowing exercises, the dumbbell row uses a pulling movement pattern that activates multiple muscles in your upper back, shoulders, core, and arms.'
                    padding_x:20
                    theme_text_color:'Custom'
                    text_color:1,1,1,1
                    halign:'center'
                    valign:'middle'
                    pos_hint:{'center_x':0.5,'center_y':0.62}
                MDLabel:
                    text:'Lunges'
                    font_style:'H4'
                    theme_text_color:'Custom'
                    halign:'center'
                    valign:'middle'
                    text_color:1,1,0,1
                    pos_hint:{'center_x':0.5,'center_y':0.48}
                MDLabel:
                    text:'The lunge is a popular leg-strengthening exercise with a multitude of variations to add variety to your workout. In addition, varying your technique allows you to emphasize different muscles or parts of those muscles.This exercise is beneficial for injury prevention, as well as rehabilitation after injuries occur.'
                    padding_x:20
                    theme_text_color:'Custom'
                    text_color:1,1,1,1
                    halign:'center'
                    valign:'middle'
                    pos_hint:{'center_x':0.5,'center_y':0.37}
                MDLabel:
                    text:'Burpees'
                    font_style:'H4'
                    theme_text_color:'Custom'
                    halign:'center'
                    valign:'middle'
                    text_color:1,1,0,1
                    pos_hint:{'center_x':0.5,'center_y':0.27}
                MDLabel:
                    text:'Burpees are a challenging exercise that work many of the major muscle groups in your body. This versatile exercise may be worth the payoff, especially if you are looking for a way to build strength and endurance, while burning calories, and boosting your cardio fitness' 
                    padding_x:20
                    theme_text_color:'Custom'
                    text_color:1,1,1,1
                    halign:'center'
                    valign:'middle'
        
                    pos_hint:{'center_x':0.5,'center_y':0.17} 
                MDBottomAppBar:
                    MDToolbar:   
                        mode:'end'
                        type:'bottom'
                        icon:'home'
                        on_action_button:  
                            root.manager.current='aim'                        

        MDNavigationDrawer:
            id : nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing : '8dp'
                padding : '8dp'
                Image:
                    source: 'aimfit2.png'
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'AimFit'
                            on_press:     
                                root.manager.current = 'aim'
                                root.manager.transition.direction = "down"
                            IconLeftWidget:
                                icon : 'home'
                                on_press:     
                                    root.manager.current = 'aim'
                                    root.manager.transition.direction = "down"
                        OneLineIconListItem:
                            text: 'About Us'
                            on_press:
                                root.manager.current = 'about' 
                                root.manager.transition.direction = "down"
                            IconLeftWidget:
                                icon : 'face-profile'
                                on_press:
                                    root.manager.current = 'about' 
                                    root.manager.transition.direction = "down"
                        OneLineIconListItem:
                            text: 'Exercise Plan'
                            on_press:
                                root.manager.current = 'exercise' 
                                root.manager.transition.direction = "up"
                            IconLeftWidget:
                                icon : 'weight-lifter'
                                on_press:     
                                    root.manager.current = 'exercise'
                                    root.manager.transition.direction = "up"                                     
                        OneLineIconListItem:
                            text: 'Logout'
                            on_press:
                                root.manager.current = 'login' 
                                root.manager.transition.direction = "down"
                            IconLeftWidget:
                                icon : 'logout'
                                on_press:     
                                    root.manager.current = 'login'
                                    root.manager.transition.direction = "down"
<OverWeightScreen>:
    name:'OverWeight'
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation:'vertical'  
                    MDToolbar:
                        title:'AimFit'
                        left_action_items:[["menu",lambda x:nav_drawer.set_state("open")]]
                    Widget:
                MDLabel:
                    text:'Exercises you need'
                    font_style:'H3'
                    theme_text_color:"Custom"
                    text_color:1,1,0,1
                    halign:'center'
                    valign:'middle'
                    height:self.texture_size[1] 
                    pos_hint : {'center_x':0.5 ,'center_y' : 0.85}    
                MDLabel:
                    text:'Walking'
                    font_style:'H4'
                    theme_text_color:'Custom'
                    halign:'center'
                    valign:'middle'
                    text_color:1,1,0,1
                    pos_hint:{'center_x':0.5,'center_y':0.75}     
                MDLabel:
                    text:'It should come as no surprise that walking is one of the best exercises to focus on if you are looking to improve your fitness and lose weight. While the benefits of walking vary depending on sex and weight, walking 1 mile can burn approximately 100 calories.Even walking slowly may be able to help you get your heart rate up, and this is what is necessary for having a great cardio exercise'
                    padding_x:20
                    theme_text_color:'Custom'
                    text_color:1,1,1,1
                    halign:'center'
                    valign:'middle'
                    pos_hint:{'center_x':0.5,'center_y':0.62}
                MDLabel:
                    text:'Modified Push-Ups'
                    font_style:'H4'
                    theme_text_color:'Custom'
                    halign:'center'
                    valign:'middle'
                    text_color:1,1,0,1
                    pos_hint:{'center_x':0.5,'center_y':0.48}
                MDLabel:
                    text:'It can be difficult to do push-ups if you are overweight, you can modify the exercise to make it easier. There are several ways you can do this if a standard push-up is too difficult.you can perform the exercise while standing up with your hands pushing against the wall instead of the floor. '
                    padding_x:20
                    theme_text_color:'Custom'
                    text_color:1,1,1,1
                    halign:'center'
                    valign:'middle'
                    pos_hint:{'center_x':0.5,'center_y':0.37}
                MDLabel:
                    text:'Side Leg Lifts'
                    font_style:'H4'
                    theme_text_color:'Custom'
                    halign:'center'
                    valign:'middle'
                    text_color:1,1,0,1
                    pos_hint:{'center_x':0.5,'center_y':0.27}
                MDLabel:
                    text:'Leg lifts are a great exercise for working out your lower body, and there are several types of leg lifts you can try. Side leg lifts, or side-lying hip abduction exercises, are one of the best types you may want to give a shot.Side leg lifts can be extremely beneficial for your lower body' 
                    padding_x:20
                    theme_text_color:'Custom'
                    text_color:1,1,1,1
                    halign:'center'
                    valign:'middle'
                    pos_hint:{'center_x':0.5,'center_y':0.17} 
                MDBottomAppBar:
                    MDToolbar:    
                        mode:'end'    
                        type:'bottom'
                        icon:'home'
                        on_action_button:
                            root.manager.current='aim'  
        MDNavigationDrawer:
            id : nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing : '8dp'
                padding : '8dp'
                Image:
                    source: 'aimfit2.png'
                    
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'AimFit'
                            on_press:     
                                root.manager.current = 'aim'
                                root.manager.transition.direction = "down"
                            IconLeftWidget:
                                icon : 'home'
                                on_press:     
                                    root.manager.current = 'aim'
                                    root.manager.transition.direction = "down"
                        OneLineIconListItem:
                            text: 'About Us'
                            on_press:
                                root.manager.current = 'about' 
                                root.manager.transition.direction = "down"
                            IconLeftWidget:
                                icon : 'face-profile'
                                on_press:
                                    root.manager.current = 'about' 
                                    root.manager.transition.direction = "down"
                        OneLineIconListItem:
                            text: 'Exercise Plan'
                            on_press:
                                root.manager.current = 'exercise' 
                                root.manager.transition.direction = "up"
                            IconLeftWidget:
                                icon : 'weight-lifter'
                                on_press:     
                                    root.manager.current = 'exercise'
                                    root.manager.transition.direction = "up"                                    
                        OneLineIconListItem:
                            text: 'Logout'
                            on_press:
                                root.manager.current = 'login' 
                                root.manager.transition.direction = "down"
                            IconLeftWidget:
                                icon : 'logout'
                                on_press:     
                                    root.manager.current = 'login'
                                    root.manager.transition.direction = "down"                                              
"""