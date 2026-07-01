# Phase 1 연습 계획: numpy · pandas · matplotlib

## 목표

이 단계의 목표는 Python으로 실험 데이터를 다루는 기본 흐름을 익히는 것이다.

데이터 파일을 불러온다.
필요한 행과 열을 선택한다.
조건에 맞는 데이터만 필터링한다.
결측치를 확인하고 처리한다.
간단한 통계량을 확인한다.
히스토그램과 산점도를 그린다.
정리한 데이터를 다시 파일로 저장한다.

이 과정을 할 수 있으면 이후 회귀 모델, PyCaret, LightGBM, RNA-seq 분석으로 넘어갈 수 있다.

---

## Day 1 — Python 스크립트 감각 익히기

### 학습 목표

- Python 코드가 위에서 아래로 실행된다는 것을 이해한다.
- 변수, 리스트, 조건문, 반복문을 사용한다.
- `.py` 파일을 만들고 실행한다.
- 실험 데이터 값을 코드로 처리하는 감각을 익힌다.

### 연습 코드

```python
particle_sizes = [120, 180, 250, 90]

for size in particle_sizes:
    if size < 200:
        print(size, "OK")
    else:
        print(size, "Too large")
```

### 확인할 것
- particle_sizes 가 무엇을 저장하는지 설명할 수 있는가?
- for가 왜 필요한지 설명할 수 있는가?
- if size < 200의 의미를 설명할 수 있는가?
- 출력 결과가 왜 그렇게 나오는지 설명할 수 있는가?

## Day 2 - numpy 기초

### 학습 목표
- numpy가 숫자 계산용 라이브러리라는 것을 이해한다.
- np.array를 만들 수 있다.
- 평균, 표준편차, 최댓값, 최솟값을 계산할 수 있다.
- 조건을 이용해 배열에서 일부 값만 고를 수 있다.

### 연습 코드

```python
import numpy as np

sizes = np.array([120, 180, 250, 90])

print("mean:", sizes.mean())
print("std:", sizes.std())
print("min:", sizes.min())
print("max:", sizes.max())
print("under 200:", sizes[sizes < 200])
```

### 확인할 것
- import numpy as np의 의미를 설명할 수 있는가?
- array와 일반 리스트의 차이를 대략 이해했는가?
- sizes.mean()이 무엇을 계산하는지 설명할 수 있는가?
- sizes[sizes < 200]의 의미를 설명할 수 있는가?

## Day 3 - pandas DataFrame 불러오기

### 학습 목표
- pandas가 표 데이터를 다루는 라이브러리라는 것을 이해한다.
- CSV 파일을 DataFrame으로 불러올 수 있다.
- head, shape, info, describe로 데이터 구조를 확인할 수 있다.
- 열 하나 또는 여러 열을 선택할 수 있다.

### 연습 코드

```python
import pandas as pd

df = pd.read_csv("formulation_data.csv")

print(df.head())
print(df.shape)
print(df.info())
print(df.describe())

print(df["particle_size_nm"])
print(df[["polymer", "particle_size_nm", "EE_percent"]])
```

### 확인할 것
- df가 무엇을 의미하는지 설명할 수 있는가?
- df.head()는 왜 먼저 확인하는가?
- df.shape의 결과가 (행, 열)이라는 것을 이해했는가?
- df["particle_size_nm"]와 df[["polymer", "EE_percent"]]의 차이를 설명할 수 있는가?

## Day 4 - 필터링과 결측치 처리

### 학습 목표
- 조건에 맞는 행만 선택할 수 있다.
- 결측치가 무엇인지 이해한다.
- 결측치 개수를 확인할 수 있다.
- 결측치를 제거하거나 평균값으로 채울 수 있다.

### 연습 코드

```python
import pandas as pd

df = pd.read_csv("formulation_data.csv")

small_particles = df[df["particle_size_nm"] < 200]
high_EE = df[df["EE_percent"] >= 70]

print("Particle size < 200")
print(small_particles)

print("EE >= 70")
print(high_EE)

print("Missing values")
print(df.isna().sum())

df_clean = df.dropna()
print(df_clean)
```

### 확인할 것
- df[df["particle_size_nm"] < 200]의 구조를 설명할 수 있는가?
- >=, <, ==의 차이를 알고 있는가?
- df.isna().sum()이 무엇을 확인하는지 설명할 수 있는가?
- dropna()를 언제 쓰면 위험할 수 있는지 설명할 수 있는가?

## Day 5 - matplotlib으로 그래프 그리기

### 학습 목표
- matplotlib이 그래프를 그리는 라이브러리라는 것을 이해한다.
- 히스토그램으로 값의 분포를 볼 수 있다.
- 산점도로 두 변수 사이의 관계를 볼 수 있다.
- 축 이름과 제목을 붙일 수 있다.
- 그래프를 이미지 파일로 저장할 수 있다.

### 연습 코드

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("formulation_data.csv")

plt.hist(df["particle_size_nm"])
plt.xlabel("Particle size (nm)")
plt.ylabel("Count")
plt.title("Particle size distribution")
plt.savefig("particle_size_histogram.png")
plt.show()

plt.scatter(df["drug_polymer_ratio"], df["EE_percent"])
plt.xlabel("Drug/polymer ratio")
plt.ylabel("EE (%)")
plt.title("Drug/polymer ratio vs EE%")
plt.savefig("ratio_vs_EE_scatter.png")
plt.show()
```

### 확인할 것
- 히스토그램이 무엇을 보여주는지 설명할 수 있는가?
- 산점도가 무엇을 보여주는지 설명할 수 있는가?
- xlabel, ylabel, title이 각각 어디에 표시되는지 알고 있는가?
- savefig로 그림 파일이 저장되는 것을 확인했는가?


## 최종 미니 과제

### 파일 만들기
formulation_data.csv라는 파일을 만들고 다음 열을 포함시킨다.

- formulation_id
- polymer
- drug
- drug_polymer_ratio
- particle_size_nm
- zeta_mV
- EE_percent

### 해야할 일
- CSV 파일을 pandas로 불러온다.
- 처음 5행을 출력한다.
- 전체 행과 열 개수를 확인한다.
- 결측치 개수를 확인한다.
- particle_size_nm < 200인 행만 필터링한다.
- EE_percent >= 70인 행만 필터링한다.
- polymer별 평균 EE_percent를 계산한다.
- particle_size_nm 히스토그램을 그린다.
- drug_polymer_ratio와 EE_percent의 산점도를 그린다.
- 정리한 데이터를 cleaned_formulation_data.csv로 저장한다.

### 최종 코드 골격

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("formulation_data.csv")

print(df.head())
print(df.shape)
print(df.info())
print(df.describe())

print(df.isna().sum())

small_particles = df[df["particle_size_nm"] < 200]
high_EE = df[df["EE_percent"] >= 70]

print(small_particles)
print(high_EE)

group_mean = df.groupby("polymer")["EE_percent"].mean()
print(group_mean)

plt.hist(df["particle_size_nm"])
plt.xlabel("Particle size (nm)")
plt.ylabel("Count")
plt.title("Particle size distribution")
plt.savefig("particle_size_histogram.png")
plt.show()

plt.scatter(df["drug_polymer_ratio"], df["EE_percent"])
plt.xlabel("Drug/polymer ratio")
plt.ylabel("EE (%)")
plt.title("Drug/polymer ratio vs EE%")
plt.savefig("ratio_vs_EE_scatter.png")
plt.show()

df_clean = df.dropna()
df_clean.to_csv("cleaned_formulation_data.csv", index=False)
```

### 완료 기준
아래를 스스로 설명할 수 있으면 이 항목은 완료로 본다.
- DataFrame이 무엇인지 설명할 수 있다.
- CSV 파일을 pandas로 불러올 수 있다.
- 필요한 열을 선택할 수 있다.
- 조건에 맞는 행만 필터링할 수 있다.
- 결측치를 확인할 수 있다.
- 히스토그램과 산점도의 차이를 설명할 수 있다.
- 정리한 데이터를 새 CSV 파일로 저장할 수 있다.