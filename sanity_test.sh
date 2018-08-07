#!/usr/bin/env bash


echo "Running binary-x XX..."
./binary-x XX > XX.out

echo "Creating test result file for XX..."
echo "00" > XX.out.tst
echo "01" >> XX.out.tst
echo "10" >> XX.out.tst
echo "11" >> XX.out.tst

diff -w XX.out XX.out.tst
if [ $? == 0 ]
then
    echo "Same"
    rm XX.out XX.out.tst
else
    echo "Different"
fi



echo "Running binary-x 1XX1..."
./binary-x X1X0X1 > X1X0X1.out

echo "Creating test result file for X1X0X1..."
echo "010001" > X1X0X1.out.tst
echo "010011" >> X1X0X1.out.tst
echo "011001" >> X1X0X1.out.tst
echo "011011" >> X1X0X1.out.tst
echo "110001" >> X1X0X1.out.tst
echo "110011" >> X1X0X1.out.tst
echo "111001" >> X1X0X1.out.tst
echo "111011" >> X1X0X1.out.tst


diff -w X1X0X1.out X1X0X1.out.tst
if [ $? == 0 ]
then
    echo "Same"
    rm X1X0X1.out X1X0X1.out.tst
else
    echo "Different"
fi