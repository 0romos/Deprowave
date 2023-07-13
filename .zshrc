export ZSH="$HOME/.oh-my-zsh"
export PNPM_HOME="/home/gast/.local/share/pnpm"
export PATH=$PATH:/home/xor/.spicetify

export "MICRO_TRUECOLOR=1"

ZSH_THEME="robbyrussell"
plugins=(git zsh-syntax-highlighting fast-syntax-highlighting zsh-autosuggestions)
source $ZSH/oh-my-zsh.sh

alias spotdl="python3 -m spotdl"
alias fh="clear && neofetch --ascii $HOME/.config/neofetch/ascii.txt"

alias pc="pwncat-cs -lp"
alias upd="sudo nala update && sudo nala upgrade"
alias battery="upower -i $(upower -e | grep BAT) | grep --color=never -E 'state|to\ full|to\ empty|percentage'"
alias f="pyaview"
alias ff="pyaview . -a"

alias ic='python3 $HOME/.scripts/custom_netface/main.py'
alias m="micro"

case ":$PATH:" in
  *":$PNPM_HOME:"*) ;;
  *) export PATH="$PNPM_HOME:$PATH" ;;
esac
