inputs=[1,2,3,2.7,3.3]
weights1=[1.5,3,5,7,9.1]
weights2=[2.2,4,6.2,8,10]
weights3=[1,2,4.3,5.1,8]

bias1=7
bias2=14
bias3=11

output=[inputs[0]*weights1[0]+inputs[1]*weights1[1]+inputs[2]*weights1[2]+inputs[3]*weights1[3]+inputs[4]*weights1[4]+bias1,
        inputs[0]*weights2[0]+inputs[1]*weights2[1]+inputs[2]*weights2[2]+inputs[3]*weights2[3]+inputs[4]*weights2[4]+bias2,
        inputs[0]*weights3[0]+inputs[1]*weights3[1]+inputs[2]*weights3[2]+inputs[3]*weights3[3]+inputs[4]*weights3[4]+bias3,
        ]

print(output)