//
//  DrawingBoard.swift
//  LazerCut
//
//  Created by Anthony Silva on 6/30/20.
//  Copyright © 2020 Anthony Silva. All rights reserved.
//

import SwiftUI
import Foundation

struct Drawingboard: View {
    
    
    func DrawingBoard() {
        
    
    func Canvas() {
        class Canvas: UIView {
            override func draw(_ rect: CGRect) {
                //Drawing
                super.draw(rect)
                
                guard let context = UIGraphicsGetCurrentContext() else {return}
                
                //lines that are being drawn
                
                lines.forEach{ (line) in
                for (i, p) in line.enumerated(){
                    if i == 0{
                        context.move(to: p)
                    }
                    else{
                        context.addLine(to: p)
                    }
            
                }
                }
                
                context.strokePath()
                
            }
            
            var lines = [[CGPoint]]()
            
            override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
                lines.append([CGPoint]())
            }
            //tracking finger as moved
            
            override func touchesMoved(_ touches: Set<UITouch>, with event: UIEvent?) {
                guard (touches.first?.location(in: self)) != nil else {return}
                
                guard let lastline = lines.popLast()else
                {
                    return
                     }
                lines.append(lastline)
               
                setNeedsDisplay()
            }
           }
        }
    
    }
  var body: Never
    
}


struct DrawingBoard_Previews: PreviewProvider {
    static var previews: some View {
        /*@START_MENU_TOKEN@*/Text("Hello, World!")/*@END_MENU_TOKEN@*/
    }
}
