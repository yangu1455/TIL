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

로컬 저장소에 원격 저장소 URL 설정하기

```shell
# 예시
git remote add origin https://github.com/yangu1455/TIL.git
```

repository 만들면 예시가 초기화면에 적혀있음.





🔵

실습 (순서만 참고)

```shell
Desktop/TIL - (master) > git status
현재 브랜치 master
커밋하도록 정하지 않은 변경 사항:
  (무엇을 커밋할지 바꾸려면 "git add <파일>..."을 사용하십시오)
  (use "git restore <file>..." to discard changes in working directory)
        수정함:        .DS_Store

커밋할 변경 사항을 추가하지 않았습니다 ("git add" 및/또는 "git commit -a"를
사용하십시오)
Desktop/TIL - (master) > git add .
Desktop/TIL - (master) > git commit -m 'TIL_0'
[master 5933014] TIL_0
 1 file changed, 0 insertions(+), 0 deletions(-)
Desktop/TIL - (master) > git status
현재 브랜치 master
커밋할 사항 없음, 작업 폴더 깨끗함
Desktop/TIL - (master) > git log
commit 5933014c5bebc4bfe8debfbccbbf780a09585ebd (HEAD -> master)
Author: yangu1455 <kunja266@hanmail.net>
Date:   Wed Jul 6 13:35:33 2022 +0900

    TIL_0

commit aaa72462f4a5ed01108e6cdb35b25d0602445393
Author: SENGA0401 <kunja266@hanmail.net>
Date:   Tue Jul 5 16:30:21 2022 +0900

    마크다운 정리
Desktop/TIL - (master) > git remote add origin https://github.com/yangu1455/TIL.git
Desktop/TIL - (master) > git push origin master
오브젝트 나열하는 중: 9, 완료.
오브젝트 개수 세는 중: 100% (9/9), 완료.
Delta compression using up to 10 threads
오브젝트 압축하는 중: 100% (8/8), 완료.
오브젝트 쓰는 중: 100% (9/9), 252.13 KiB | 31.52 MiB/s, 완료.
Total 9 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), done.
To https://github.com/yangu1455/TIL.git
 * [new branch]      master -> master
Desktop/TIL - (master) > git config --global core.editor "code --wait"
Desktop/TIL - (master) > git push origin master
Everything up-to-date
```



