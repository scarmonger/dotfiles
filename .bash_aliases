alias df="df -h -x squashfs -x tmpfs -x devtmpfs"
alias lsmount="mount | column -t"
alias extip="curl icanhazip.com"

alias bi="sudo apt --fix-broken install"
alias di="sudo dpkg -i"
alias i="sudo apt install"

alias so="source ~/.bashrc"
alias upgrade="sudo apt update && sudo apt dist-upgrade"
alias speedtest="curl -s https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py | python3 -"

# top 5 processes that using most memory
alias mem5="ps auxf | sort -nr -k 4 | head -5"
alias cpu10="ps auxf | sort -nr -k 3 | head -10"
# wmctrl -lG // to check all windows opened
alias fa="wmctrl -r firefox -e 0,20,50,1224,800"
alias rr="ranger"
alias rs="sudo ranger"
alias sus="i3lock -etfi ~/Documents/wp.png; systemctl suspend"
alias cala="cal 2022"
alias cam="ffplay /dev/video0"

# git
alias gs="git status"
alias gas="git add . && git commit -m 'add' && git push"
alias gpl="git pull"

alias gd="cd ~/Documents/github/dataon/ && nvim"
alias gt="cd ~/Documents/github/tech/ && nvim"
alias gp="cd ~/Documents/github/personal/ && nvim"

alias gp="cd ~/Documents/ && yt-dlp -f '\''bestaudio'\'' "

# alias extres="xrandr --output LVDS-1 --auto --output VGA-1 --primary --mode 1600x900 --left-of LVDS-1"

alias e230="xrandr --output LVDS-1 --auto --output VGA-1 --primary --auto --left-of LVDS-1"
alias etp13="xrandr --output eDP-1 --auto --output HDMI-1 --auto --left-of eDP-1"

alias mirror="echo xrandr --output VGA-1 --auto --scale-from 1366x768 --output LVDS-1"

alias tr="tmux attach -t ranger || tmux new -s ranger"
alias tv="tmux attach -t nvim || tmux new -s nvim"
alias td="tmux attach -t download || tmux new -s download"

export EDITOR='nvim'
export VISUAL='nvim'
export RANGER_LOAD_DEFAULT_RC='FALSE'
export CUSTOM_NVIM_PATH='/usr/local/bin/nvim.appimage'
