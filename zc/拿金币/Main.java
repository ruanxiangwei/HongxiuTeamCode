package com.DP.拿金币;

import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		int N = 0 ;
		Scanner scan = new Scanner(System.in);
		N = scan.nextInt();
		int arr[][] = new int[N][N];
		for(int i = 0; i < N; i++) {
			for(int j = 0;j < N; j++) {
				arr[i][j] = scan.nextInt();
			}
		}
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < N; j++) {
				if(i == 0 && j > 0) {
					arr[i][j] = arr[i][j] + arr[i][j-1];
				}
				else if(j == 0 && i > 0) {
					arr[i][j] = arr[i][j] + arr[i-1][j];
				}
				else {
					if(i != 0 && j != 0)
						arr[i][j] = arr[i][j] + Math.max(arr[i-1][j],arr[i][j-1]);
				}
			}
		}
		System.out.println(arr[N-1][N-1]);
	}
}
