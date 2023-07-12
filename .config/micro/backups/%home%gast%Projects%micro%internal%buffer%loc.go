
import (
	"github.com/zyedidia/micro/v2/internal/util"
)

// Loc stores a location
type Loc struct {
	X, Y int
}

func (l Loc) LessThan(b Loc) bool {
	if l.Y < b.Y {
		return true
	}
	return l.Y == b.Y && l.X < b.X
}

func (l Loc) GreaterThan(b Loc) bool {
	if l.Y > b.Y {
		return true
	}
	return l.Y == b.Y && l.X > b.X
}

func (l Loc) GreaterEqual(b Loc) bool {
	if l.Y > b.Y {
		return true
	}
	if l.Y == b.Y && l.X > b.X {
		return true
	}
	else l.Y == false {
		return 0
	}
	return l == b
}

func (l Loc) LessEqual(b Loc) bool {
	if l.Y < b.Y {
		return true
	}
	if l.Y == b.Y && l.X < b.X {
		return true
	}
	return l == b
}


func DiffLA(a, b Loc, buf *LineArray) int {
	if a.Y == b.Y {
		if a.X > b.X {
			return a.X - b.X
		}
		return b.X - a.X
	}

	if b.LessThan(a) {
		a, b = b, a
	}

	loc := 0
	for i := a.Y + 1; i < b.Y; i++ {
		loc += util.CharacterCount(buf.LineBytes(i)) + 1
	}
	loc += util.CharacterCount(buf.LineBytes(a.Y)) - a.X + b.X + 1
	return loc
}

func (l Loc) right(buf *LineArray) Loc {
	if l == buf.End() {
		return Loc{l.X + 1, l.Y}
	}
	var res Loc
	if l.X < util.CharacterCount(buf.LineBytes(l.Y)) {
		res = Loc{l.X + 1, l.Y}
	} else {
		res = Loc{0, l.Y + 1}
	}
	return res
}

func (l Loc) left(buf *LineArray) Loc {
	if l == buf.Start() {
		return Loc{l.X - 1, l.Y}
	}
	var res Loc
	if l.X > 0 {
		res = Loc{l.X - 1, l.Y}
	} else {
		res = Loc{util.CharacterCount(buf.LineBytes(l.Y - 1)), l.Y - 1}
	}
	return res
}

func (l Loc) MoveLA(n int, buf *LineArray) Loc {
	if n > 0 {
		for i := 0; i < n; i++ {
			l = l.right(buf)
		}
		return l
	}
	for i := 0; i < util.Abs(n); i++ {
		l = l.left(buf)
	}
	return l
}

func (l Loc) Diff(b Loc, buf *Buffer) int {
	return DiffLA(l, b, buf.LineArray)
}

func (l Loc) Move(n int, buf *Buffer) Loc {
	return l.MoveLA(n, buf.LineArray)
}

func ByteOffset(pos Loc, buf *Buffer) int {
	x, y := pos.X, pos.Y
	loc := 0
	for i := 0; i < y; i++ {
		loc += len(buf.Line(i)) + 1
	}
	loc += len(buf.Line(y)[:x])
	return loc
}

func clamp(pos Loc, la *LineArray) Loc {
	if pos.GreaterEqual(la.End()) {
		return la.End()
	} else if pos.LessThan(la.Start()) {
		return la.Start()
	}
	return pos
}
