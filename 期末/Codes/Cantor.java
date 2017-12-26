import java.awt.*;
import javax.swing.*;
import java.lang.*;

public class Cantor extends JApplet{
	public void init() {
		new Cantor();
	}
	
	public void frameSet() {
		Cantor shapes = new Cantor();
		JFrame fra = new JFrame("WELCOME");
		fra.getContentPane().add(shapes, BorderLayout.CENTER);
		fra.setSize(new Dimension(670, 400));
		fra.setResizable(false);
		fra.setVisible(true);
	}
	
	public static void main(String args[]) {
		new Cantor().frameSet();
		
	}
	
	public void paint(Graphics g) {
		g.setColor(Color.BLACK);
		drawShape(g,100,100,800,100);
	}
	
	public void drawShape(Graphics g, double ax, double ay, double bx, double by) {
		double c = 1;
		
		if((bx - ax) < c) {
			g.drawLine((int)ax, (int)ay, (int)bx, (int)by);
		}
		else {
			double cx = 0;
			double cy = 0;
			double dx = 0;
			double dy = 0;
			
			g.drawLine((int)ax, (int)ay, (int)bx, (int)by);
			
			cx = ax + (bx - ax) / 3;
			cy = ay + 50;
			dx = bx - (bx - ax) / 3;
			dy = by + 50;
			ay = ay + 50;
			by = by + 50;
			
			drawShape(g, ax, ay, cx, cy);
			drawShape(g, dx, dy, bx, by);
		}
		
	}
}
