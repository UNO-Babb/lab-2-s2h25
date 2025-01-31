#FutureTime.py
#Name:
#Date:
#Assignment:

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
   now = datetime.datetime.now()
   currentHour = (now.hour - 6) % 24
   currentMinute = (now.minute)


  #Ask for additional hours and minutes
   addMins = int(input("Enter minutes to add: "))
   addHours = int(input("Enter hours to add: "))                    

  #Calculate future time
   futureMinute = (currentMinute + addMins) % 60
   extraHours = (currentMinute + addMins) // 60
   futureHour = (currentHour + addHours + extraHours) % 24
  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"
   print(f"Future Time: {futureHour:02}:{futureMinute:02}")

if __name__ == '__main__':
  main()
