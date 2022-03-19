alias rr="ranger"
alias rs="sudo ranger"
alias sus="i3lock -etfi /home/xyz/Documents/eOS/tea.png; systemctl suspend"
alias cala="cal 2022"
alias cam="ffplay /dev/video0"

alias gs="git status"
alias ga="git add ."
alias gm="git commit -m 'add'"
alias gps="git push"
alias gpl="git pull"

alias gd="cd ~/Documents/github/dataon/ && nvim"
alias gt="cd ~/Documents/github/tech/ && nvim"
alias gp="cd ~/Documents/github/personal/ && nvim"

alias gp="cd ~/Documents/ && yt-dlp -f '\''bestaudio'\'' "

alias x0="xrandr --output LVDS-1 --auto --output VGA-1 --primary --mode 1600x900 --left-of LVDS-1"

alias x2="echo xrandr --output VGA-1 --auto --scale-from 1366x768 --output LVDS-1"

alias tr="tmux attach -t ranger || tmux new -s ranger"
alias tv="tmux attach -t nvim || tmux new -s nvim"
alias td="tmux attach -t download || tmux new -s download"

export EDITOR='nvim'
export VISUAL='nvim'
export RANGER_LOAD_DEFAULT_RC='FALSE'
export CUSTOM_NVIM_PATH='/usr/local/bin/nvim.appimage'
