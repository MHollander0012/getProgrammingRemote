minIn = input("Enter time in minutes: ");
minIn = int(minIn);
hr = int(minIn / 60);
min = minIn % 60;
min = int(min);

print(hr, " hours and", min, " minutes");