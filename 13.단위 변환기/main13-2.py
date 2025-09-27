def convert_temperature(value, from_unit, to_unit):
    """온도 변환 함수"""
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return value * 9/5 + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Celsius" and to_unit == "Celsius":
        return value
    elif from_unit == "Fahrenheit" and to_unit == "Fahrenheit":
        return value
    else:
        return None

def convert_length(value, from_unit, to_unit):
    """길이 변환 함수"""
    if from_unit == "Meter" and to_unit == "Feet":
        return value * 3.281
    elif from_unit == "Feet" and to_unit == "Meter":
        return value / 3.281
    elif from_unit == "Meter" and to_unit == "Meter":
        return value
    elif from_unit == "Feet" and to_unit == "Feet":
        return value
    else:
        return None

def convert_weight(value, from_unit, to_unit):
    """무게 변환 함수"""
    if from_unit == "Kilogram" and to_unit == "Pound":
        return value * 2.205
    elif from_unit == "Pound" and to_unit == "Kilogram":
        return value / 2.205
    elif from_unit == "Kilogram" and to_unit == "Kilogram":
        return value
    elif from_unit == "Pound" and to_unit == "Pound":
        return value
    else:
        return None

def main():
    """메인 함수"""
    print("=" * 60)
    print("🔄 단위 변환기")
    print("=" * 60)
    print("지원하는 변환:")
    print("🌡️  온도: Celsius ↔ Fahrenheit")
    print("📏 길이: Meter ↔ Feet")
    print("⚖️  무게: Kilogram ↔ Pound")
    print("=" * 60)
    
    while True:
        try:
            print("\n변환할 값을 입력하세요 (종료하려면 'q' 입력):")
            value_input = input("값: ").strip()
            
            if value_input.lower() == 'q':
                print("프로그램을 종료합니다. 👋")
                break
            
            value = float(value_input)
            
            print("\n변환할 단위를 선택하세요:")
            print("1. 온도 (Celsius ↔ Fahrenheit)")
            print("2. 길이 (Meter ↔ Feet)")
            print("3. 무게 (Kilogram ↔ Pound)")
            
            choice = input("선택 (1-3): ").strip()
            
            if choice == "1":
                print("\n온도 단위를 선택하세요:")
                print("1. Celsius → Fahrenheit")
                print("2. Fahrenheit → Celsius")
                temp_choice = input("선택 (1-2): ").strip()
                
                if temp_choice == "1":
                    result = convert_temperature(value, "Celsius", "Fahrenheit")
                    print(f"\n🌡️  {value}°C = {result:.2f}°F")
                elif temp_choice == "2":
                    result = convert_temperature(value, "Fahrenheit", "Celsius")
                    print(f"\n🌡️  {value}°F = {result:.2f}°C")
                else:
                    print("❌ 잘못된 선택입니다.")
                    
            elif choice == "2":
                print("\n길이 단위를 선택하세요:")
                print("1. Meter → Feet")
                print("2. Feet → Meter")
                length_choice = input("선택 (1-2): ").strip()
                
                if length_choice == "1":
                    result = convert_length(value, "Meter", "Feet")
                    print(f"\n📏 {value}m = {result:.2f}ft")
                elif length_choice == "2":
                    result = convert_length(value, "Feet", "Meter")
                    print(f"\n📏 {value}ft = {result:.2f}m")
                else:
                    print("❌ 잘못된 선택입니다.")
                    
            elif choice == "3":
                print("\n무게 단위를 선택하세요:")
                print("1. Kilogram → Pound")
                print("2. Pound → Kilogram")
                weight_choice = input("선택 (1-2): ").strip()
                
                if weight_choice == "1":
                    result = convert_weight(value, "Kilogram", "Pound")
                    print(f"\n⚖️  {value}kg = {result:.2f}lb")
                elif weight_choice == "2":
                    result = convert_weight(value, "Pound", "Kilogram")
                    print(f"\n⚖️  {value}lb = {result:.2f}kg")
                else:
                    print("❌ 잘못된 선택입니다.")
            else:
                print("❌ 잘못된 선택입니다.")
                
        except ValueError:
            print("❌ 숫자를 입력해주세요.")
        except Exception as e:
            print(f"❌ 오류가 발생했습니다: {e}")

if __name__ == '__main__':
    main()
