import kivymd
from kivymd.app  import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton , MDRectangleFlatButton ,MDIconButton ,MDFloatingActionButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
from kivymd.uix.list import MDList , TwoLineListItem ,OneLineListItem, TwoLineIconListItem ,IconLeftWidget , TwoLineAvatarIconListItem , ImageLeftWidget
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.datatables import MDDataTable
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from data import DataBase
from helpers import screenss

# Window.size = (360,640)

def invalid_form():
    pop  = MDDialog(title="Invalid Entry", text="Invaild Email or Password")
    pop.open()

def invalid_entry():
    pop1 = MDDialog(title = "Invalid entry",text = "You have entered invalid values")
    pop1.open()
    
class info():
    def bmi_1(self):
        e_button = MDFlatButton(text='Exercise Plan' , on_release = self.switch1)
        self.p = MDDialog(title = "Serverly Underweight",text = "Your bmi is less then 16 this means that you are serverly underweight. Your diet plan is to Eat more of vegetables and fruits especially bananas, mangoes, watermelon, pomegranate, carrots, beans, broccoli, spinach, grapes, beetroot etc. Include good quality MUFA & PUFA rich oils.Ditch fast food for a while and drink plenty of water.",buttons=[e_button])
        self.p.open()
        
    def bmi_2(self):
        e_button = MDFlatButton(text='Exercise Plan' , on_release = self.switch1)
        self.p = MDDialog(title = "Underweight",text = "Your bmi is between 16 and 18.5 this means that you are underweight. Your diet plan is to consume around 2200 calories a day.Try to increase the amount of food you eat 3 time a day. try to consume eggs, milk, almond, walnuts, fruit shakes, smoothie, fresh juices, vegitables curry and fruits, drick around 8 glass of water per day.",buttons=[e_button])
        self.p.open()

    def bmi_3(self):
        e_button = MDFlatButton(text='Exercise Plan' , on_release = self.switch2)
        self.p = MDDialog(title = "Normal Healthy",text = "Your bmi is between 18.5 and 25 this means that you are in normal healthy condition. A healthy eating plan will lower your risk for heart disease and other health conditions. You Diet plan is to, Emphasizes vegetables, fruits, whole grains, and fat-free or low-fat dairy products. Includes lean meats, poultry, fish, beans, eggs, and nuts. Limits saturated and trans fats, sodium, and added sugars. Controls portion sizes.",buttons=[e_button])
        self.p.open()

    def bmi_4(self):
        e_button = MDFlatButton(text='Exercise Plan' , on_release = self.switch3)
        self.p = MDDialog(title = "Overweight",text = "Your bmi is between 25 and 30 this means that you are Overweight. Your diet plan is to , Cut Down On Carbohydrates, Increase The Protein Intake, Keep Fat To A Minimum, Eat Less Energy - Dense Foods, Avoid “Feel Bad” Foods, Reduce The Intake Of Salt, Start With Soup, Get Enough B – Vitamins, Get Enough Vitamin D, Eat Vitamin C,  Get Enough Calcium, Eat Zinc and Consume Iodine.",buttons=[e_button])
        self.p.open()

    def bmi_5(self):
        e_button = MDFlatButton(text='Exercise Plan' , on_release = self.switch3)
        self.p = MDDialog(title = "Moderatly Obese",text = "Your bmi is between 30 and 35 this means that you are moderatly obese. Your diet plan is to consume around 1600 calories a day. Try to eat oranges, apples, melons, guava, berries, and avoid banana, mango, litchi, grapes and other sugary fruits. Moderately include almonds, walnuts and flax seeds inure diet. Fish, chicken, egg whites can be consumed in moderation. Include healthy oils e.g. olive, mustard, sunflower oil. ",buttons=[e_button])
        self.p.open()

    def bmi_6(self):
        e_button = MDFlatButton(text='Exercise Plan' , on_release = self.switch3)
        self.p = MDDialog(title = "Serverly Obese",text = "Your bmi is greater than 35 this means that you are sererly obese. Your diet plan should include foods that have complex carbs. To get enough complex carbs, try to include brown rice, whole wheat bread, oatmeal, potatoes, sweet potatoes, and legumes. it should also include Protein-rich foods include chicken, beans, yogurt, eggs, fish, beef, lentils, chickpeas, beans, and so on.",buttons=[e_button])
        self.p.open()
    
    def switch1(self,obj):
        self.manager.current = "UnderWeight"
        self.p.dismiss()
        
    def switch2(self,obj):
        self.manager.current = "NormalWeight"
        self.p.dismiss()
        
    def switch3(self,obj):
        self.manager.current = "OverWeight"
        self.p.dismiss()               

class Login(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    
    def loginBtn(self):
        if db.validate(self.email.text, self.password.text):
            self.reset()
            self.manager.current = "aim"
            
        else:
            invalid_form()

    def reset(self):
        self.email.text = ""
        self.password.text = ""
    
class Account(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    
    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count("@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)
                self.reset()
                self.manager.current= "login"
            else:
                invalid_form()
        else:
            invalid_form()

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""
        
    
class Main(Screen):
    pass
class About(Screen):
    pass
class Bmi(Screen,info):
    weight = ObjectProperty(None)
    h = ObjectProperty(None)
    ttttext = ObjectProperty(None)
            
    def calculate(self):
        try:
            if self.weight.text != "" and self.h.text != "":
                val1 = float(self.weight.text)
                val2 = float(self.h.text)
                self.value = round(float(val1 / (val2)**2),1)
                self.reset()
            else:
                invalid_entry()    
        except:
            self.reset()
            invalid_entry()
            
        if self.value < 16:
            self.bmi_1()
        elif self.value >= 16 and self.value <= 18.5 :
            self.bmi_2()
        elif self.value > 18.5 and self.value <= 25 :
            self.bmi_3()       
        elif self.value > 25 and self.value <= 30 :
            self.bmi_4()
        elif self.value > 30 and self.value <= 35 :
            self.bmi_5()
        elif self.value > 35  :
            self.bmi_6()

        self.ttttext.text = "Your B.M.I is:  " + str(self.value)
                                              
    def reset(self):
        self.weight.text = ""
        self.h.text = ""

class Exercise(Screen):
    pass
class UnderWeightScreen(Screen):
    pass
class NormalWeightScreen(Screen):
    pass
class OverWeightScreen(Screen):
    pass

db = DataBase("users.txt")
sm = ScreenManager()
sm.add_widget(Login(name= "login"))
sm.add_widget(Account(name="account"))
sm.add_widget(Main(name="aim"))
sm.add_widget(About(name="about"))
sm.add_widget(Bmi(name="bmi"))
sm.add_widget(Exercise(name="exercise"))
class AimfitApp(MDApp):
        def build(self):
            self.theme_cls.primary_palette = "Yellow"
            self.theme_cls.primary_hue = "A700"
            self.theme_cls.theme_style = "Dark"
            screen = Builder.load_string(screenss)
            return screen      
App = AimfitApp()        
App.run()