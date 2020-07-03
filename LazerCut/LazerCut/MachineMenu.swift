//
//  MachineMenu.swift
//  LazerCut
//
//  Created by Anthony Silva on 6/29/20.
//  Copyright © 2020 Anthony Silva. All rights reserved.
//

import SwiftUI
import Foundation

struct MachineMenu: View {
    @State private var linedrag = CGSize.zero
    @State private var startpoint = Int.self
    var body: some View {
        NavigationView{
            VStack{
            Drawingboard(body: Never)
            
            }
        
    }
    }
    
}

struct MachineMenu_Previews: PreviewProvider {
    static var previews: some View {
        MachineMenu()
    }
}

