# ๐ธ Git/GitHub 2์ผ์ฐจ ๐ธ

----



๐ต 

Git ์ค์  ๋ณ๊ฒฝํ๊ธฐ

git config --global user.name "์์ด๋"

git config --global user.email "์ด๋ฉ์ผ์ฃผ์(๋๋๋ก ๊นํ๋ธ์ ์ฐ๊ฒฐํ๋๊ฒ ํธํจ)"



ํ์ธํ๊ธฐ

git config --global --list





๐ต

MAC ์์ Git ๋ธ๋์น ์ ๋ณด ์ค์ ํ๊ธฐ

1. ํฐ๋ฏธ๋์ ์ฐ๋ค.
2. Code ~/.zshrc   ๋ผ๊ณ  ๋ช๋ น์ด๋ฅผ ์๋ ฅํ๋ค.
3. ๊ทธ๋ฌ๋ฉด vscode ๊ฐ ์ผ์ง๊ณ  .zshrc ํ์ผ ์ด๋ฆฐ๋ค.

> โ๏ธ ์ค๋ฅ์ ์ฐธ๊ณ ํ  ํ์ด์ง
>
> https://smilehugo.tistory.com/entry/code-command-is-not-working-on-mac-how-to-solve

4. ๋ฌธ์์ ์๋ ๋ด์ฉ ๋ณต๋ถ

   ```shell
   # Find and set branch name var if in git repository.
   
   function git_branch_name()
   {
     branch=$(git symbolic-ref HEAD 2> /dev/null | awk 'BEGIN{FS="/"} {print $NF}')
     if [[ $branch == "" ]];
     then
       :
     else
       echo '- ('$branch')'
     fi
   }
   
   # Enable substitution in the prompt.
   setopt prompt_subst
   
   # Config for prompt. PS1 synonym.
   prompt='%2/ $(git_branch_name) > '
   ```

5. ์ด๋ ค์๋ ๋ชจ๋  ํฐ๋ฏธ๋ ์ข๋ฃ ํ ์ฌ์์
6. git init ํ๋ฉด master ํ์ ํ์ธ





๐ต

vscode๋ฅผ ์๋ํฐ๋ก ํ์ฉํ๊ธฐ

ํฐ๋ฏธ๋์

```shell
git config --global core.editor "code --wait" 		
```

์๋ ฅํ๊ธฐ





๐ต

mac ์์ code. ๊ฐ ๋จนํ์ง ์๋ ๊ฒฝ์ฐ

1. vscode ์ด๊ณ  cmd + shift + p ๋ก ๊ฒ์์ฐฝ(?) ์ด๊ณ  shell command ์๋ ฅ

2. shell command: install 'code' command in path  ๋๋ฅด๊ธฐ

3. ํฐ๋ฏธ๋ ์ข๋ฃ ํ ์ฌ์คํ

4. ์ ํฐ๋ฏธ๋์์ code .  ์๋ ฅ





๐ต

๋ก์ปฌ ์ ์ฅ์์ ์๊ฒฉ ์ ์ฅ์ URL ์ค์ ํ๊ธฐ

```shell
# ์์
git remote add origin https://github.com/yangu1455/TIL.git
```

repository ๋ง๋ค๋ฉด ์์๊ฐ ์ด๊ธฐํ๋ฉด์ ์ ํ์์.





๐ต

์ค์ต (์์๋ง ์ฐธ๊ณ )

```shell
Desktop/TIL - (master) > git status
ํ์ฌ ๋ธ๋์น master
์ปค๋ฐํ๋๋ก ์ ํ์ง ์์ ๋ณ๊ฒฝ ์ฌํญ:
  (๋ฌด์์ ์ปค๋ฐํ ์ง ๋ฐ๊พธ๋ ค๋ฉด "git add <ํ์ผ>..."์ ์ฌ์ฉํ์ญ์์ค)
  (use "git restore <file>..." to discard changes in working directory)
        ์์ ํจ:        .DS_Store

์ปค๋ฐํ  ๋ณ๊ฒฝ ์ฌํญ์ ์ถ๊ฐํ์ง ์์์ต๋๋ค ("git add" ๋ฐ/๋๋ "git commit -a"๋ฅผ
์ฌ์ฉํ์ญ์์ค)
Desktop/TIL - (master) > git add .
Desktop/TIL - (master) > git commit -m 'TIL_0'
[master 5933014] TIL_0
 1 file changed, 0 insertions(+), 0 deletions(-)
Desktop/TIL - (master) > git status
ํ์ฌ ๋ธ๋์น master
์ปค๋ฐํ  ์ฌํญ ์์, ์์ ํด๋ ๊นจ๋ํจ
Desktop/TIL - (master) > git log
commit 5933014c5bebc4bfe8debfbccbbf780a09585ebd (HEAD -> master)
Author: yangu1455 <kunja266@hanmail.net>
Date:   Wed Jul 6 13:35:33 2022 +0900

    TIL_0

commit aaa72462f4a5ed01108e6cdb35b25d0602445393
Author: SENGA0401 <kunja266@hanmail.net>
Date:   Tue Jul 5 16:30:21 2022 +0900

    ๋งํฌ๋ค์ด ์ ๋ฆฌ
Desktop/TIL - (master) > git remote add origin https://github.com/yangu1455/TIL.git
Desktop/TIL - (master) > git push origin master
์ค๋ธ์ ํธ ๋์ดํ๋ ์ค: 9, ์๋ฃ.
์ค๋ธ์ ํธ ๊ฐ์ ์ธ๋ ์ค: 100% (9/9), ์๋ฃ.
Delta compression using up to 10 threads
์ค๋ธ์ ํธ ์์ถํ๋ ์ค: 100% (8/8), ์๋ฃ.
์ค๋ธ์ ํธ ์ฐ๋ ์ค: 100% (9/9), 252.13 KiB | 31.52 MiB/s, ์๋ฃ.
Total 9 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), done.
To https://github.com/yangu1455/TIL.git
 * [new branch]      master -> master
Desktop/TIL - (master) > git config --global core.editor "code --wait"
Desktop/TIL - (master) > git push origin master
Everything up-to-date
```



