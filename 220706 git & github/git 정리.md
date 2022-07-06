# 🌸 Git/GitHub 2일차 🌸

----



🔵 

Git 설정 변경하기

git config --global user.name "아이디"

git config --global user.email "이메일주소(되도록 깃허브와 연결하는게 편함)"



확인하기

git config --global --list





🔵

MAC 에서 Git 브랜치 정보 설정하기

1. 터미널을 연다.
2. Code ~/.zshrc   라고 명령어를 입력한다.
3. 그러면 vscode 가 켜지고 .zshrc 파일 열린다.

> ✔️ 오류시 참고할 페이지
>
> https://smilehugo.tistory.com/entry/code-command-is-not-working-on-mac-how-to-solve

4. 문서에 아래 내용 복붙

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

5. 열려있는 모든 터미널 종료 후 재시작
6. git init 하면 master 표시 확인





🔵

vscode를 에디터로 활용하기

터미널에

```shell
git config --global core.editor "code --wait" 				
```

입력하기





🔵

mac 에서 code. 가 먹히지 않는 경우

1. vscode 열고 cmd + shift + p 로 검색창(?) 열고 shell command 입력

2. shell command: install 'code' command in path  누르기

3. 터미널 종료 후 재실행

4. 새 터미널에서 code .  입력





🔵

실습화면 (순서만 참고)

![220706 실습화면](git 정리.assets/220706 실습화면.png)

