A, B = map(int, input().split())

C = int(input())

total_M = A * 60 + B + C

end_H = (total_M // 60) % 24
end_M = total_M % 60

print(end_H, end_M)
