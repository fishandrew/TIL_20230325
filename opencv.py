import cv2 as cv
print(cv.__version__) # 버전 출력

img = cv.imread('cat.jpg',1) # 이미지 읽기
cv.imshow('Test Image',img) # 이미지를 화면에 표시
cv.waitKey(0)  # 입력값을 기다림
cv.destroyAllWindows() # 이미지 윈도우 삭제

cv.imwrite('Cat.jpg', img) # 이미지를 다른 파일로 저장
