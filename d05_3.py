# 입력 예시
# s = '@#~I NeVEr DrEamEd AbouT SuCCeSs, i woRkEd foR iT.!>!'

# 출력 예시
# 'I never dreamed about success, i worked for it.'
import re
s = '@#~I NeVEr DrEamEd AbouT SuCCeSs, i woRkEd foR iT.!>!'
new_s = re.sub(r"[^\uAC00-\uD7A30-9a-zA-Z\s]", "", s)
print(f"'{new_s.capitalize()}.'")