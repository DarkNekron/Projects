#include <stdio.h>
#include <string.h>
#include <conio.h>

int main ()
{
	int ans, key;
	char in[260];
	printf("Press 1 to Encrypt file.\nPress 2 to Decrypt file.\n");
	scanf("%d", &ans);
	printf("Enter File Name -\n");
	scanf("%s", &in);
	printf("Enter Key -\n");
	scanf("%d", &key);
	if (ans == 1)
	{
		char c;
		FILE *fin;
		FILE *fout;
		fin = fopen(in, "rb");
		strcpy(in, "output");//Creates a file with no extention
		fout = fopen(in, "wb");
		while (!feof(fin))
		{
			c = fgetc(fin);
			int temp = (c + key);
			fputc((char)temp, fout);
		}
		fclose(fin);
		fclose(fout);
	}
	else if (ans == 2)
	{
		char c;
		FILE *fin;
		FILE *fout;
		fin = fopen(in, "rb");
		strcpy(in, "decryptedoutput");//Make sure you add the same extension as the original file
		fout = fopen(in, "wb");
		while (!feof(fin))
		{
			c = fgetc(fin);
			int temp = (c - key);
			fputc((char)temp, fout);
		}
		fclose(fin);
		fclose(fout);
	}
	getch();
}
