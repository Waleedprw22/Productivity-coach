const TableHeader = () => {
    return (
      <thead>
        <tr>
          <th className="px-4 py-5 border-b-2 border-gray-200 bg-lightblack text-center text-base font-semibold text-darkwhite uppercase tracking-wider lg:text-sm">
            Rank
          </th>
          <th className="px-4 py-5 border-b-2 border-gray-200 bg-lightblack text-left text-base font-semibold text-darkwhite uppercase tracking-wider lg:text-sm">
            User ID
          </th>
          <th className="px-4 py-5 border-b-2 border-gray-200 bg-lightblack text-center text-base font-semibold text-darkwhite uppercase tracking-wider lg:text-sm xs:hidden">
            Hours
          </th>
        </tr>
      </thead>
    );
  };
  
  export default TableHeader;