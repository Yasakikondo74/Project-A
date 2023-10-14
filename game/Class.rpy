init python:
    class MC:
        def __init__(self):
            self.name = "Player"
            self.location = "Bedroom"
            self.Character_selection = 1
            self.genders = "Male"
            self.charisma = 0
            self.job = "Unemployed"
            self.income = 5.00
            self.salery_increase = 1
            self.money = 0
            self.upgrade_points = 0
        
        def Location_bed(self):
            self.location = "Bedroom"
        def Location_school(self):
            self.location = "School"
        def Location_workplace(self):
            self.location = "Workplace"

        def Change_character1(self):
            self.Character_selection = 1
        def Change_character2(self):
            self.Character_selection = 2

        def upgrade_income(self):
            if self.income == 5 and self.upgrade_points >= 1:
                self.income = 10
                self.upgrade_points -= 1
            elif self.income == 10 and self.upgrade_points >= 2:
                self.income = 20
                self.upgrade_points -= 1
            elif self.income == 20 and self.upgrade_points >= 3:
                self.income = 50
                self.upgrade_points -= 1
            elif self.income == 50 and self.upgrade_points >= 4:
                self.income = 100
                self.upgrade_points -= 1
        
        def upgrade_raw_money(self):
            if self.salery_increase == 1 and self.upgrade_points >= 1:
                self.salery_increase = 2
                self.upgrade_points -= 1
            elif self.salery_increase == 2 and self.upgrade_points >= 2:
                self.salery_increase = 3
                self.upgrade_points -= 1

    mc = MC()

    class girl:
        def __init__(self, name, age, love, type, status):
            self.name = name
            self.age = age
            self.love = love
            self.status = status

        def Status(self):
            if self.type == "Normal":
                if -5 < self.love < 5:
                    self.status = "Acquainted" 
                elif -25 < self.love < -5:
                    self.status = "Hate"
                elif self.love < -25:
                    self.status = "Despise"
                elif self.love < 100 and self.day_spent > 5:
                    self.status = "Liked"
                elif self.love < 1000 and self.day_spent > 25:
                    self.status = "Loved"
            else:
                return

    # class World:
    #     def __init__(self, minute, hour, day, month, year, population, weekday):
    #         self.minute = minute
    #         self.hour = hour
    #         self.day = day
    #         self.month = month
    #         self.year = year
    #         self.population = population
    #         self.weekday = (self.year, self.month, self.day).weekday()

    #     def Time_Reset(self): #TIME RESET
    #         if self.minute == 60:
    #             self.minute = 0
    #             self.hour += 1
    #         if self.hour == 24
    #             self.day += 1
    #             self.hour = 0
    #         if self.month in [1, 3, 5, 7, 12, 8]:
    #             if self.day == 31:
    #                 self.day = 0
    #                 self.month += 1
    #         if self.month in [4, 6, 9, 10, 11]:
    #             if self.day == 30:
    #                 self.day = 0
    #                 self.month += 1
    #         if self.year % 2:
    #             if self.month == "Febuary":
    #                 if self.day == 29:
    #                     self.day = 0
    #         else:
    #             if self.month == "Febuary":
    #                 if self.day == 28:
    #                     self.day = 0
    #         def population_contorl(self):

    #             if self.day in [7, 14, 21, 28]:
    #                 self.population = self.population * n

