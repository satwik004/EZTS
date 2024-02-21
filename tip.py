def main():
   dollar = dollar_to_float(input())
   percentage = percentage_to_float(input())
   tip = (dollar*percentage)/100
   print(f"Leave ${tip:.2f}")

def dollar_to_float(dollar):
   dollar = dollar[1:]
   return [int(dollar)]
def percentage_to_float(percentage):
   return [int(percentage)]

main()