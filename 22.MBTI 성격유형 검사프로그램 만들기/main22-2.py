from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    questions = [
        "대체로 사람들과 어울리는 것을 좋아한다.",
        "논쟁보다는 타협하는 것이 좋다고 생각한다.",
        "대개 계획을 세우는 것을 좋아한다.",
        "새로운 일에 도전하는 것을 좋아한다.",
        "감정을 드러내는 것보다는 이성적으로 생각하는 것이 좋다고 생각한다.",
        "대체로 조용한 분위기를 좋아한다.",
        "사람들과의 대화에서 자주 말하는 편이다.",
        "어떤 일을 할 때 체계적으로 처리하는 편이다.",
        "강한 경쟁심이 있다.",
        "주로 자신의 감정에 따라 일을 처리한다."
    ]

    return render_template('index.html', questions=questions)

@app.route('/result', methods=['POST'])
def result():
    try:
        # 모든 질문에 답변했는지 확인
        answers = {}
        for i in range(1, 11):
            answer = request.form.get('q' + str(i))
            if not answer:
                return render_template('error.html', message="모든 질문에 답변해주세요.")
            answers[i] = int(answer)

        # MBTI 점수 계산
        scores = {"E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0}
        
        # 각 질문별로 점수 계산
        for i in range(1, 11):
            answer = answers[i]
            
            # E/I (외향/내향)
            if i in [1, 7]:  # 사람들과 어울리는 것, 자주 말하는 편
                if answer >= 4:
                    scores['E'] += 1
                else:
                    scores['I'] += 1
            
            # S/N (감각/직관)
            if i in [3, 8]:  # 계획 세우는 것, 체계적 처리
                if answer >= 4:
                    scores['S'] += 1
                else:
                    scores['N'] += 1
            
            # T/F (사고/감정)
            if i in [2, 5, 10]:  # 타협, 이성적 사고, 감정에 따라 처리
                if answer >= 4:
                    scores['F'] += 1
                else:
                    scores['T'] += 1
            
            # J/P (판단/인식)
            if i in [4, 6, 9]:  # 새로운 일 도전, 조용한 분위기, 경쟁심
                if answer >= 4:
                    scores['P'] += 1
                else:
                    scores['J'] += 1

        # MBTI 결과 결정
        result = ""
        result += "E" if scores['E'] > scores['I'] else "I"
        result += "S" if scores['S'] > scores['N'] else "N"
        result += "T" if scores['T'] > scores['F'] else "F"
        result += "J" if scores['J'] > scores['P'] else "P"

        return render_template('result.html', result=result, scores=scores)
    
    except Exception as e:
        return render_template('error.html', message=f"오류가 발생했습니다: {str(e)}")

if __name__ == '__main__':
    app.run()
